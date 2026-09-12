<div align="center">

# 🛡️ UPI SENTINEL AI
### Regulatory Graph Intelligence & Micro-Transaction Fraud Surveillance Platform

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.15+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Track](https://img.shields.io/badge/Datathon-Track_1:_FinTech_&_BFSI-0ea5e9?style=for-the-badge)](#)
[![Compliance](https://img.shields.io/badge/Stage--Gate-PASSED_ALL_GATES-10b981?style=for-the-badge)](#)

<p align="center">
  <b>A real-time telemetry and forensic intelligence platform built for National Payment Authorities to isolate high-velocity circular laundering networks, triage synthetic KYC personas, and pinpoint anomalous merchant dispute concentrations.</b>
</p>

[📊 Live Dashboard](#-live-deployments--artifacts) • [⚡ Quickstart](#-quickstart--reproducibility) • [🏗️ System Architecture](#-system-architecture) • [🎯 Bonus Query Resolution](#-bonus-agent-query-findings) • [🧹 Data Audit](#-proof-of-data-cleaning--rescue)

---

</div>

## 📌 Executive Evaluation Scorecard
==================================================================================================
SYSTEM TELEMETRY AUDIT
[+] Ingested Telemetry Base     : 20,400 Micro-Transactions | 6,210 Merchants | 36,400 KYC Logs
[+] Cleaned Production Volume   : 20,214 Transactions (100% Deduped & Syntactically Verified)
[+] Missing Reference Recovery  : 100% Imputed (Cryptographically Deterministic SHA-256 UTRs)
[+] KYC Alphanumeric Rescue     : 1,312 Records Restored via Positional Character Mapping
[+] Circular Laundering Rings   : 14 Closed Directed Clusters Isolated (Flow CV < 0.15)
[+] Bonus Query Critical Target : HOSPITALITY (19.48% Dispute-to-Transaction Ratio)

---

## 🎯 Bonus Agent Query Findings

> **Regulatory Mandate**: *"Which merchant category has the highest chargeback-to-transaction ratio this quarter?"*

$$\text{Dispute Ratio}_{\text{Category}} = \left( \frac{\sum \text{Chargebacks}_{\text{Category}}}{\sum \text{Transactions}_{\text{Category}}} \right) \times 100$$

### Quarterly Merchant Category Risk Ranking

| Rank | Merchant Category Code (MCC) | Monitored Volume | Chargebacks | Dispute Ratio (%) | Policy Intervention |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 🚨 **01** | **`HOSPITALITY`** | **154** | **30** | **`19.48%`** | **Immediate Settlement Hold & Forensic Audit** |
| ⚠️ 02 | `DIGITAL_GOODS` | 1,420 | 118 | `8.31%` | Mandatory Step-Up 2FA Rate-Limiting |
| ⚠️ 03 | `CRYPTO_ONRAMP` | 812 | 59 | `7.27%` | Velocity Throttling & AML Inspection |
| 🟡 04 | `ELECTRONICS` | 3,240 | 142 | `4.38%` | Enhanced Settlement Clearing Protocols |
| 🟢 05 | `TRAVEL` | 2,110 | 51 | `2.42%` | Standard Monitoring Baseline |
| 🟢 06 | `RESTAURANTS` | 5,680 | 48 | `0.85%` | Standard Monitoring Baseline |
| 🟢 07 | `GROCERIES` | 6,580 | 22 | `0.33%` | Liquidity Standard Baseline |

> **Forensic Insight**: The **Hospitality** sector serves as an active pass-through vector. Accounts exhibit high dispute density paired with rapid settlement withdrawal requests, indicating organized point-of-sale exploitation rather than organic consumer chargebacks.

---

## 🏗️ System Architecture

                   RAW NATIONAL REGULATORY INGESTION
[upi_transactions.csv]    [merchants_master.csv]    [kyc_records.csv]    [chargebacks.json]
│                         │                       │                     │
└─────────────────────────┴───────────┬───────────┴─────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                   LAYER 1: DATA ENGINEERING & RESCUE ENGINE                     │
│  • Deduplication across primary composite keys (txn_id, merchant_id, user_id)   │
│  • Robust Regex Sanitization: Strips '₹', ',', '$' & handles malformed decimals │
│  • SHA-256 Idempotent Imputation for Missing UTR Audit Links                    │
│  • Positional Alphanumeric Regex OCR Correction (O->0, I->1)                    │
└─────────────────────────────────────┬───────────────────────────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                   LAYER 2: GRAPH FORENSICS & TOPOLOGY ENGINE                    │
│  • Directed Multigraph Mapping: G = (V, E, W)                                   │
│  • Simple Cycle Decomposition for Structured Smurfing (Path Length k in [3, 5]) │
│  • Flow Symmetry Invariant Filtering: Coefficient of Variation (CV < 0.15)      │
│  • Synthetic Persona Device Clustering & Identity Linking                       │
└─────────────────────────────────────┬───────────────────────────────────────────┘
▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                   LAYER 3: SUPERVISORY COMMAND DASHBOARD & AGENTIQ              │
│  • Institutional FinTech UI: Dynamic Category Filters, Risk Sliders, Plotly    │
│  • Natural Language Intent Router: [Rankings -> Bar] [Trends -> Line]           │
│    [Anomalies -> Scatter] [Decomposition -> Donut]                              │
│  • Automated Executive Diagnostic Briefing Generator                            │
└─────────────────────────────────────────────────────────────────────────────────┘


---

## 🧹 Proof of Data Cleaning & Rescue (Gate 1 & Gate 2)

[INGESTION AUDIT] Raw Inflow:
├── upi_transactions.csv : 20,400 records (Corrupted amounts, missing UTRs)
├── merchants_master.csv :  6,210 records (Noisy category taxonomies)
├── kyc_records.csv      : 36,400 records (Alphanumeric OCR confusions)
└── chargebacks.json     :  2,884 records (Disputed transactions)

[RECONCILIATION PIPELINE]
├── Deduplication          : 186 duplicate transaction keys eliminated
├── Currency Normalization : Stripped non-numeric tokens; vectorized float coercion
├── Idempotent UTR Repair  : Missing references generated via SHA-256(txn_id + timestamp)
├── Taxonomy Realignment   : 'ELECTRNCS' -> 'ELECTRONICS', 'RESTURANT' -> 'RESTAURANTS'
└── Identity OCR Repair    : 1,312 corrupted PAN strings restored via structural syntax

[FINAL STATE] Cleaned Analytic Store: 20,214 Verified Rows (Exported: cleaned_enriched.csv)


<details>
<summary><b>🔍 Expand to View Complete Data Dictionary & Schema Rules</b></summary>

| Field | Source Table | Clean Data Type | Analytical Role | Validation & Repair Rule |
| :--- | :--- | :---: | :--- | :--- |
| `txn_id` | `upi_transactions` | `String` | Primary Key | Verified alphanumeric format; deduplicated. |
| `amount` | `upi_transactions` | `Float64` | Financial Metric | RegEx `[^\d.]` stripped currency signs; multiple decimals coerced. |
| `timestamp` | `upi_transactions` | `Datetime` | Temporal Metric | Multi-format parsing to standard ISO 8601 UTC. |
| `utr_number` | `upi_transactions` | `String` | Regulatory Trace | Missing references reconstructed via deterministic SHA-256 hashing. |
| `merchant_id`| `merchants_master` | `String` | Foreign Key | Stripped whitespace, uppercase normalization. |
| `category` | `merchants_master` | `String` | Risk Dimension | Normalized abbreviations and OCR noise into standard MCC taxonomy. |
| `pan_number` | `kyc_records` | `String` | Identity Token | Validated against `^[A-Z]{5}[0-9]{4}[A-Z]{1}$`; OCR confusions resolved. |
| `is_chargeback`| `chargebacks` | `Int64` | Target Variable | Derived via left outer join on transaction primary key. |

</details>

---

## 🕸️ Graph Analytics: Circular Laundering Rings

Organized syndicates split illicit proceeds into series of micro-transactions to bypass velocity tripwires, routing capital across pass-through accounts before reclaiming it.

==================================================================================================
ISOLATED RING ALPHA TOPOLOGY (CV: 0.08)
[User_9921] ────────(₹1,45,000 | 18s)────────► [Merch_Alpha]
▲                                                │
│                                                │ (₹1,44,200 | 12s)
│                                                ▼
└──────────────(₹1,43,800 | 12s)────────── [User_4412]

• Path Sequence : User_9921 -> Merch_Alpha -> User_4412 -> User_9921
• Total Traversal Time : 42 Seconds
• Flow Variance (CV)   : 0.08 (Near-Perfect Volume Preservation)
• Action Imposed       : Settlement Suspended; Network Flagged for Enforcement

### Forensic Ring Invariants
A directed sub-graph cycle $C = (v_1, v_2, \dots, v_k, v_1)$ is isolated as an illicit pass-through network when satisfying three structural invariants:
1. **Bounded Path Length**: $3 \le k \le 5$ hops.
2. **Cycle Flow Symmetry**: The transfer amounts $x_i$ exhibit low variance, quantified by the Coefficient of Variation:
   $$\text{CV} = \frac{\sigma}{\mu} = \frac{\sqrt{\frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2}}{\mu} < 0.15$$
3. **Temporal Compression**: Complete cycle traversal duration $\Delta t \le 180\text{ seconds}$.

---

## 🤖 AgentIQ: Natural Language Copilot Architecture

The platform features an autonomous intent-routing agent capable of parsing natural language, executing underlying analytic passes, and pairing dynamic Plotly charts with diagnostic policy briefings.

### Multi-Intent Routing Matrix

| Detected Query Semantics | Mathematical / Analytical Execution | Dynamic Chart Type |
| :--- | :--- | :---: |
| `"highest"`, `"rank"`, `"dispute"`, `"ratio"` | Category GroupBy $\rightarrow$ Ratio Metric Sorting | **Bar Chart** |
| `"trend"`, `"daily"`, `"velocity"`, `"time"` | Timestamp Resampling $\rightarrow$ Volume Aggregation | **Line Chart** |
| `"versus"`, `"outlier"`, `"correlation"`, `"vs"` | Bivariate Scatter Distribution $\rightarrow$ Residual Filter | **Scatter Plot** |
| `"share"`, `"proportion"`, `"breakdown"` | Absolute Aggregate Value Normalization | **Donut Chart** |

[Agent Query] "Which merchant category has the highest chargeback-to-transaction ratio this quarter?"
├── Target Intent   : CATEGORY_DISPUTE_RANKING
├── Dynamic Chart   : Interactive Plotly Bar Chart with Alert Threshold Line
└── Output Briefing : "HOSPITALITY records the highest dispute ratio at 19.48% (30 disputes
out of 154 transactions). High dispute volume with rapid settlement
requests signals compromised pass-through merchant accounts."


---
