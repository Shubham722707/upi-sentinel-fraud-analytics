import os
import re
import glob
import hashlib
import numpy as np
import pandas as pd

desktop_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))

def find_file(pattern):
    search_paths = [
        os.path.join(desktop_dir, "**", pattern),
        os.path.join(os.getcwd(), "**", pattern),
    ]
    for sp in search_paths:
        matches = glob.glob(sp, recursive=True)
        if matches:
            return matches[0]
    return None

TX_PATH = find_file("track1_upi_transactions.csv")
MERCHANT_PATH = find_file("track1_merchants_master.csv")
KYC_PATH = find_file("track1_kyc_records.csv")
CB_PATH = find_file("track1_chargebacks.json")

print("Locating files:")
print(f"  Transactions: {TX_PATH}")
print(f"  Merchants:    {MERCHANT_PATH}")
print(f"  KYC:          {KYC_PATH}")
print(f"  Chargebacks:  {CB_PATH}")

if not all([TX_PATH, MERCHANT_PATH, KYC_PATH, CB_PATH]):
    print("\n[ERROR] Could not find one or more required files!")
    exit(1)

def find_col(df, candidates, default=None):
    clean_cols = {re.sub(r'[\s_]+', '', str(c)).lower(): c for c in df.columns}
    for cand in candidates:
        cand_clean = re.sub(r'[\s_]+', '', cand).lower()
        if cand_clean in clean_cols:
            return clean_cols[cand_clean]
    for clean_key, orig in clean_cols.items():
        if any(cand.lower() in clean_key for cand in candidates):
            return orig
    return default

# 1. Load Data
df_tx = pd.read_csv(TX_PATH)
df_merchants = pd.read_csv(MERCHANT_PATH)
df_kyc = pd.read_csv(KYC_PATH)
df_cb = pd.read_json(CB_PATH)

print(f"\nRaw Counts -> Tx: {len(df_tx)}, Merchants: {len(df_merchants)}, KYC: {len(df_kyc)}, CB: {len(df_cb)}")

# Detected columns from your actual terminal output:
# ['txn_id', 'timestamp', 'user_id', 'merchant_id', 'amount', 'utr', 'mcc', 'status']
tx_id_col = 'txn_id'
merchant_id_col = find_col(df_merchants, ['merchant_id', 'id'], df_merchants.columns[0])
user_id_col = find_col(df_kyc, ['user_id', 'id'], df_kyc.columns[0])

# 2. Deduplicate
df_tx = df_tx.drop_duplicates(subset=[tx_id_col])
df_merchants = df_merchants.drop_duplicates(subset=[merchant_id_col])
df_kyc = df_kyc.drop_duplicates(subset=[user_id_col])

# 3. Clean Amount and Timestamps
cleaned_amounts = (
    df_tx['amount'].astype(str)
    .str.replace(r'[^\d.]', '', regex=True)
    .apply(lambda x: re.sub(r'(\..*?)\..*', r'\1', x))
)
df_tx['amount'] = pd.to_numeric(cleaned_amounts, errors='coerce')
df_tx['amount'] = df_tx['amount'].fillna(df_tx['amount'].median())

df_tx['timestamp'] = pd.to_datetime(df_tx['timestamp'], errors='coerce')

# 4. Impute Missing UTRs
utr_col = 'utr' if 'utr' in df_tx.columns else 'utr_number'
if utr_col not in df_tx.columns:
    df_tx[utr_col] = np.nan

missing_mask = df_tx[utr_col].isna() | (df_tx[utr_col].astype(str).str.strip().isin(['', 'nan', 'None']))

def generate_utr(row):
    t_val = str(row.get(tx_id_col, ''))
    d_val = str(row.get('timestamp', ''))
    payload = f"{t_val}_{d_val}".encode('utf-8')
    digits = re.sub(r'\D', '', hashlib.sha256(payload).hexdigest())
    return (digits + "123456789012")[:12]

df_tx.loc[missing_mask, utr_col] = df_tx[missing_mask].apply(generate_utr, axis=1)

# 5. Clean Merchant Categories
cat_col = find_col(df_merchants, ['category', 'merchant_category', 'mcc', 'type'], df_merchants.columns[1])
df_merchants[cat_col] = (
    df_merchants[cat_col].astype(str).str.upper().str.strip()
    .replace({'ELECTRNCS': 'ELECTRONICS', 'GROCERIES_': 'GROCERIES', 'RESTURANT': 'RESTAURANTS'})
)

# 6. Merge Datasets
enriched = df_tx.merge(df_merchants, on='merchant_id', how='left', suffixes=('', '_m'))

cb_tx_col = find_col(df_cb, ['txn_id', 'transaction_id', 'tx_id'], df_cb.columns[0])
enriched = enriched.merge(df_cb, left_on=tx_id_col, right_on=cb_tx_col, how='left', suffixes=('', '_cb'))

cb_id_col = find_col(df_cb, ['chargeback_id', 'cb_id', 'dispute_id'], df_cb.columns[0])
enriched['is_chargeback'] = enriched[cb_id_col].notna().astype(int)

# 7. Save Processed Output to CSV (Avoids PyArrow type issues)
output_file = "cleaned_enriched.csv"
enriched.to_csv(output_file, index=False)
print(f"\n[SUCCESS] Cleaned data saved to {output_file} ({len(enriched)} rows)")

# 8. Bonus Agent Query Calculation
cb_summary = enriched.groupby(cat_col)['is_chargeback'].agg(['count', 'sum']).reset_index()
cb_summary['ratio'] = (cb_summary['sum'] / cb_summary['count']) * 100
cb_summary = cb_summary.sort_values(by='ratio', ascending=False)

print("\n=======================================================")
print("             BONUS AGENT QUERY RESULT                 ")
print("=======================================================")
if not cb_summary.empty:
    top_cat = cb_summary.iloc[0]
    print(f"Merchant Category with highest chargeback ratio: {top_cat[cat_col]}")
    print(f"Chargeback-to-Transaction Ratio: {top_cat['ratio']:.2f}%")
    print(f"Disputed Transactions: {int(top_cat['sum'])} / {int(top_cat['count'])}")
print("=======================================================\n")