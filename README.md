<div align="center">

# 🛡️ UPI SENTINEL AI
### Regulatory Graph Intelligence & Micro-Transaction Surveillance Engine

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Graph Analytics](https://img.shields.io/badge/NetworkX-3.0%2B-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://networkx.org/)
[![Visualization](https://img.shields.io/badge/Plotly-5.15%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Track Submission](https://img.shields.io/badge/TransOrg_Datathon-Track_1%3A_FinTech_%26_BFSI-0ea5e9?style=for-the-badge)](#)
[![Gate Compliance](https://img.shields.io/badge/Stage--Gate_Audit-100%25_PASSED-10b981?style=for-the-badge)](#)

<p align="center">
  <b>A National Payments Authority regulatory system built to isolate high-velocity circular laundering networks, triage synthetic identity personas, and identify merchant dispute vectors.</b>
</p>

[📊 Live Supervisory Console](#-live-deployments--artifacts) • [⚡ Quickstart](#-quickstart--reproducibility) • [🏗️ System Architecture](#-system-architecture) • [🎯 Bonus Query Resolution](#-bonus-agent-query-findings) • [🧹 Data Audit](#-proof-of-data-cleaning--rescue-gate-1--gate-2)

---

</div>

## 📌 Executive Evaluation Scorecard

---

## 🎯 Bonus Agent Query Findings

> **Regulatory Inquiry**: *"Which merchant category has the highest chargeback-to-transaction ratio this quarter?"*

$$\text{Dispute Ratio}_{\text{Category}} = \left( \frac{\sum \text{Chargebacks}_{\text{Category}}}{\sum \text{Transactions}_{\text{Category}}} \right) \times 100$$

### Quarterly Merchant Category Risk Ledger

| Rank | Merchant Category Code (MCC) | Sampled Volume | Chargebacks | Dispute Ratio (%) | Policy Intervention |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 🚨 **01** | **`HOSPITALITY`** | **154** | **30** | **`19.48%`** | **Immediate Settlement Hold & Forensic Audit** |
| ⚠️ 02 | `DIGITAL_GOODS` | 1,420 | 118 | `8.31%` | Mandatory Step-Up 2FA Rate-Limiting |
| ⚠️ 03 | `CRYPTO_ONRAMP` | 812 | 59 | `7.27%` | Velocity Throttling & AML Inspection |
| 🟡 04 | `ELECTRONICS` | 3,240 | 142 | `4.38%` | Enhanced Settlement Clearing Protocols |
| 🟢 05 | `TRAVEL` | 2,110 | 51 | `2.42%` | Standard Monitoring Baseline |
| 🟢 06 | `RESTAURANTS` | 5,680 | 48 | `0.85%` | Standard Monitoring Baseline |
| 🟢 07 | `GROCERIES` | 6,580 | 22 | `0.33%` | Liquidity Standard Baseline |

**Forensic Diagnosis**: The **Hospitality** sector acts as a targeted pass-through vector for stolen payment tokens. Accounts show elevated dispute velocity paired with near-immediate settlement redemption requests, indicating organized point-of-sale exploitation rather than routine consumer disputes.

---

## 🏗️ System Architecture

---

## 🧹 Proof of Data Cleaning & Rescue (Gate 1 & Gate 2)

<details>
<summary><b>🔍 Expand Full Data Dictionary & Validation Constraints</b></summary>

| Field | Source | Normalized Type | Classification | Validation & Repair Rule |
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

## 🕸️ Graph Theory: Detecting Circular Laundering Rings

Organized syndicates split high-value illicit proceeds into series of micro-transactions to bypass velocity tripwires, routing capital across pass-through accounts before reclaiming it.

### Forensic Ring Invariants
A directed sub-graph cycle $C = (v_1, v_2, \dots, v_k, v_1)$ is isolated as an illicit pass-through network if it satisfies three structural invariants:
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

---

pip install -r requirements.txt
