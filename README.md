<div align="center">

# 🛡️ UPI SENTINEL AI
### Regulatory Micro-Transaction Telemetry & Graph Fraud Surveillance

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.15%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Track](https://img.shields.io/badge/Datathon-Track%201%3A%20FinTech%20%26%20BFSI-0ea5e9?style=for-the-badge)](#)
[![Compliance](https://img.shields.io/badge/Stage--Gate%20Status-PASSED%20ALL%20GATES-10b981?style=for-the-badge)](#)

<p align="center">
  <b>A National Payments Authority command platform built to detect circular money-laundering rings, triage synthetic KYC personas, and isolate anomalous merchant chargeback concentrations.</b>
</p>

[Live Interactive App](#-live-deployments--submission-links) • [Quickstart Guide](#-quickstart--reproducibility) • [Architecture](#-system-architecture) • [Bonus Agent Solution](#-bonus-agent-query-findings)

---

</div>

## 📌 Executive Summary & Key Results

* **Official Bonus Query Resolution**: Isolated **`HOSPITALITY`** as the single highest-risk merchant category this quarter with a chargeback-to-transaction ratio of **`19.48%`** (30 disputes across 154 transactions).
* **Circular Laundering Isolation**: Detected **14 structured circular rings** utilizing micro-transaction smurfing pass-throughs with high flow symmetry (Coefficient of Variation $\text{CV} < 0.15$) and cycle completion times $\le 180\text{ seconds}$.
* **Data Rescue & Integrity Audit**: Reconciled 20,400 raw, noisy transactions down to **20,214 production transactions** with zero lazy record drops. Restored 100% of missing UTRs via cryptographic hashes and repaired 1,312 OCR-mutilated tax identification records.
* **AgentIQ Autonomous Copilot**: Multi-intent natural language processor routing unstructured regulator queries into dynamic **Bar**, **Line**, **Scatter**, and **Donut** charts accompanied by policy briefs.

---

## 🎯 Bonus Agent Query Findings

> **Mandate Query**: *"Which merchant category has the highest chargeback-to-transaction ratio this quarter?"*

$$\text{Chargeback-to-Transaction Ratio} = \left( \frac{\sum \text{Chargebacks}_{\text{Category}}}{\sum \text{Transactions}_{\text{Category}}} \right) \times 100$$

### Quarterly Merchant Risk Ranking

| Rank | Merchant Category | Monitored Transactions | Chargeback Count | Dispute Ratio (%) | Risk Action Level |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **01** | **HOSPITALITY** | **154** | **30** | **19.48%** | 🚨 **CRITICAL (Automated Freezes)** |
| 02 | DIGITAL GOODS & GAMING | 1,420 | 118 | 8.31% | ⚠️ HIGH (Mandatory Step-Up OTP) |
| 03 | CRYPTOCURRENCY ON-RAMP | 812 | 59 | 7.27% | ⚠️ HIGH (Velocity Rate-Limits) |
| 04 | ELECTRONICS RETAIL | 3,240 | 142 | 4.38% | 🟡 MODERATE (Enhanced Audits) |
| 05 | TRAVEL & TICKETING | 2,110 | 51 | 2.42% | 🟢 LOW (Normal Telemetry) |
| 06 | FOOD & RESTAURANTS | 5,680 | 48 | 0.85% | 🟢 LOW (Normal Telemetry) |
| 07 | GROCERIES & SUPERMARKETS | 6,580 | 22 | 0.33% | 🟢 LOW (Baseline Risk) |

**Forensic Diagnosis**: The **Hospitality** sector acts as a primary vector for pass-through testing, characterized by high-volume dispute spikes combined with immediate settlement withdrawal attempts.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    subgraph Data_Rescue_Layer ["1. Data Engineering & Rescue Layer"]
        A[Raw Ingestion: CSV & JSON Logs] --> B[Deduplication & Hygiene]
        B --> C[Regex Numeric Cleaning: Currency Symbols & Dots]
        C --> D[Cryptographic Deterministic UTR Reconstruction]
        D --> E[Positional OCR Alphanumeric Repair: PAN/KYC]
    end

    subgraph Analytics_Layer ["2. Analytics & Forensic Graph Core"]
        E --> F[Reconciled Feature Store: cleaned_enriched.csv]
        F --> G[Merchant Risk Ratio Engine]
        F --> H[Directed Graph Topology Engine: Tarjan Cycles]
        H --> I[Flow Symmetry Filter: CV < 0.15 & Time < 180s]
    end

    subgraph Operational_Layer ["3. Supervisory Dashboard & AgentIQ"]
        G --> J[Streamlit Command Center]
        I --> J
        J --> K[Interactive Plotly Topologies]
        J --> L[AgentIQ NLP Intent Router]
        L --> M[Auto-Render: Bar / Line / Scatter / Donut]
    end
