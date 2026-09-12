# UPI Sentinel AI: National Fraud Ring & Merchant Analytics
**Track 1: FinTech & BFSI | TransOrg AgentIQ Datathon**

UPI Sentinel is a production-grade regulatory surveillance platform built for National Payment Authorities. It ingests high-velocity, noisy telemetry data, automatically repairs identity and transaction logs, and deploys a directed graph cycle engine to isolate circular money-laundering rings. The platform is paired with an interactive AgentIQ Copilot that translates natural language queries into automated charts and executive briefings.

---

## 1. Executive Summary & Core Results

* **Bonus Agent Query Resolution**: *"Which merchant category has the highest chargeback-to-transaction ratio this quarter?"*
  * **Answer**: **`HOSPITALITY`** exhibits the highest dispute ratio at **`19.48%`** (30 chargebacks across 154 transactions).
* **Laundering Ring Isolation**: Detected **14 structured circular rings** operating micro-transaction smurfing cycles with high flow symmetry (Coefficient of Variation < 0.15) and cycle velocity under 180 seconds.
* **Data Rescue Audit**: Ingested 20,400 raw transaction logs. Rather than dropping broken records, the pipeline deterministically imputed missing UTRs via SHA-256 hashes and restored 1,312 OCR-corrupted tax identification records. Final clean baseline: **20,214 production transactions**.

---

## 2. Project Architecture & Repository Structure
upi_fraud_project/
├── data/
│   ├── raw/                 # Raw transactions, merchants, KYC, and chargebacks (excluded from git)
│   └── processed/           # Reconciled, cleaned parquet/CSV datasets
├── src/
│   ├── init.py
│   └── agent/
│       ├── init.py
│       └── agent_engine.py  # Text-to-Chart Agent & NLP Intent Router
├── tests/
│   └── test_agent.py        # Automated test suite for agent edge-cases
├── app.py                   # Dark-mode Streamlit supervisory command center
├── run_pipeline.py          # ETL pipeline, regex cleaning, OCR & UTR repair
├── requirements.txt         # Pinned production dependencies
└── README.md                # This documentation

---

## 3. Data Dictionary & Cleaning Rules

| Table Name | Column | Data Type | Description | Cleaning / Validation Rule Applied |
| :--- | :--- | :--- | :--- | :--- |
| `upi_transactions` | `txn_id` | String | Transaction Primary Key | Deduped to ensure absolute uniqueness. |
| `upi_transactions` | `amount` | Float64 | Transaction value | Regex `[^\d.]` applied to strip currency symbols (`₹`, `,`, `$`); double dots resolved. |
| `upi_transactions` | `timestamp`| Datetime | Transaction event time | Standardized mixed formats to ISO 8601. |
| `upi_transactions` | `utr_number`| String | Unique Reference | Missing UTRs reconstructed via idempotent `SHA256(txn_id + timestamp)` mapping to preserve audit links. |
| `merchants_master` | `category` | String | Merchant Category | OCR noise stripped; uppercase standardization (e.g., `ELECTRNCS` -> `ELECTRONICS`). |
| `kyc_records` | `pan_number` | String | Tax ID (PAN) | Validated against `^[A-Z]{5}[0-9]{4}[A-Z]{1}$`; repaired OCR confusions (e.g., `O` vs `0`, `I` vs `1`). |

---

## 4. Quickstart & Reproducibility

### Prerequisites
* Python 3.9+
* A virtual environment (`venv`)

### Installation
Clone the repository and install dependencies:
```bash
git clone [ https://github.com/Shubham722707/upi-sentinel-fraud-analytics.git ]

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate



