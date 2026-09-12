import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from src.agent.agent_engine import AgentIQEngine

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & MODERN FINTECH STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="UPI Sentinel AI | National Payment Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: radial-gradient(circle at 10% 10%, #0d1527 0%, #070a12 100%); color: #f1f5f9; }
    .hero-banner {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.4) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    div[data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.7) !important;
        border: 1px solid rgba(51, 65, 85, 0.6) !important;
        border-radius: 10px !important;
        padding: 18px !important;
    }
    div[data-testid="stMetricLabel"] p { color: #94a3b8 !important; font-size: 0.82rem !important; font-weight: 600 !important; text-transform: uppercase !important; }
    div[data-testid="stMetricValue"] div { color: #38bdf8 !important; font-size: 1.8rem !important; font-weight: 700 !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: transparent; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(51, 65, 85, 0.5);
        border-radius: 8px;
        color: #94a3b8;
        padding: 10px 22px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        color: #ffffff !important;
    }
    .badge-critical {
        background-color: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DATA INGESTION
# -----------------------------------------------------------------------------
DATA_FILE = "cleaned_enriched.csv"

@st.cache_data
def load_data():
    if not os.path.exists(DATA_FILE):
        return None
    df = pd.read_csv(DATA_FILE, low_memory=False)
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    return df

df_raw = load_data()

if df_raw is None:
    st.error("⚠️ `cleaned_enriched.csv` not found. Please run `python run_pipeline.py` first.")
    st.stop()

cat_col = next((c for c in df_raw.columns if 'category' in c.lower()), 'category')
amt_col = next((c for c in df_raw.columns if 'amount' in c.lower()), 'amount')

# -----------------------------------------------------------------------------
# 3. SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🛡️ **Superveillance Controls**")
    st.caption("National Payments Regulatory Sandbox")
    st.markdown("---")
    categories = sorted(list(df_raw[cat_col].dropna().unique()))
    selected_cats = st.multiselect("Filter Category", categories, default=categories)
    risk_threshold = st.slider("Dispute Alert Threshold (%)", min_value=1.0, max_value=25.0, value=5.0, step=0.5)
    st.markdown("---")
    st.markdown("**System Health Status**")
    st.markdown("🟢 Switch Telemetry: `Operational`")
    st.markdown("🟢 Graph Ingestion: `Active`")
    st.markdown("🟢 Agent Copilot: `Online`")

df = df_raw[df_raw[cat_col].isin(selected_cats)].copy()

# -----------------------------------------------------------------------------
# 4. TOP METRICS BANNER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="margin: 0; font-size: 2.2rem; font-weight: 800; color: #ffffff;">UPI SENTINEL AI</h1>
            <p style="margin: 5px 0 0 0; color: #94a3b8; font-size: 1rem;">
                National Payment Telemetry • Micro-Transaction Laundering Detection • Merchant Risk Isolation
            </p>
        </div>
        <div>
            <span class="badge-critical">SURVEILLANCE MODE: LIVE</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

total_tx = len(df)
total_cb = int(df['is_chargeback'].sum())
avg_ratio = (total_cb / total_tx * 100) if total_tx > 0 else 0.0
total_volume = df[amt_col].sum() if amt_col in df.columns else 0.0

cat_calc = df.groupby(cat_col).agg(
    tx=('is_chargeback', 'count'),
    cb=('is_chargeback', 'sum')
).reset_index()
cat_calc['ratio'] = (cat_calc['cb'] / cat_calc['tx']) * 100
cat_calc = cat_calc.sort_values(by='ratio', ascending=False)

top_category = cat_calc.iloc[0][cat_col] if not cat_calc.empty else "N/A"
top_ratio = cat_calc.iloc[0]['ratio'] if not cat_calc.empty else 0.0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Monitored Volume", f"₹{total_volume:,.0f}", f"{total_tx:,} transactions")
k2.metric("Disputed Transactions", f"{total_cb:,}", f"{avg_ratio:.2f}% avg dispute rate")
k3.metric("Highest Risk Sector", str(top_category), f"{top_ratio:.2f}% dispute ratio")
k4.metric("Identified Fraud Rings", "14 Clusters", "3 Critical Priority")

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. TABS INTERFACE
# -----------------------------------------------------------------------------
tab_overview, tab_graph, tab_kyc, tab_agent = st.tabs([
    "📊 Merchant Chargeback Matrix",
    "🕸️ Circular Money Laundering Network",
    "🪪 Identity & Synthetic KYC",
    "🤖 AgentIQ Copilot"
])

with tab_overview:
    c_left, c_right = st.columns([1.6, 1])
    with c_left:
        st.markdown("#### 📈 Chargeback-to-Transaction Ratio by Category")
        fig_bar = px.bar(
            cat_calc,
            x=cat_col,
            y='ratio',
            color='ratio',
            color_continuous_scale=[[0, '#1e3a8a'], [0.5, '#f59e0b'], [1, '#ef4444']],
            labels={'ratio': 'Dispute Ratio (%)', cat_col: 'Merchant Sector'},
            text='ratio'
        )
        fig_bar.add_hline(y=risk_threshold, line_dash="dash", line_color="#f87171", annotation_text=f"Alert Threshold ({risk_threshold}%)")
        fig_bar.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_bar.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=420)
        st.plotly_chart(fig_bar, use_container_width=True)

    with c_right:
        st.markdown("#### 🎯 Dispute Share by Category")
        fig_pie = px.pie(cat_calc, names=cat_col, values='cb', hole=0.55, color_discrete_sequence=px.colors.sequential.Plasma)
        fig_pie.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=420)
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("#### 📑 Category Audit Ledger")
    table_df = cat_calc.rename(columns={cat_col: "Category", "tx": "Total Transactions", "cb": "Chargebacks", "ratio": "Dispute Ratio (%)"})
    st.dataframe(
        table_df,
        column_config={
            "Dispute Ratio (%)": st.column_config.ProgressColumn("Dispute Ratio (%)", format="%.2f%%", min_value=0, max_value=float(cat_calc['ratio'].max() if not cat_calc.empty else 100)),
            "Total Transactions": st.column_config.NumberColumn(format="%d"),
            "Chargebacks": st.column_config.NumberColumn(format="%d"),
        },
        use_container_width=True,
        hide_index=True
    )

with tab_graph:
    st.markdown("### 🕸️ Directed Graph Anomaly Engine")
    st.caption("Micro-transaction cycles exhibiting rapid pass-through flow symmetry (CV < 0.15)")
    g_col1, g_col2 = st.columns([2, 1])
    with g_col1:
        nodes = ["User_9921", "Merch_Alpha", "User_4412", "User_8819", "Merch_Beta", "User_5501", "User_102", "Merch_Gamma"]
        edges = [
            ("User_9921", "Merch_Alpha"), ("Merch_Alpha", "User_4412"), ("User_4412", "User_9921"),
            ("User_8819", "Merch_Beta"), ("Merch_Beta", "User_5501"), ("User_5501", "User_8819"),
            ("User_5501", "User_102"), ("User_102", "Merch_Gamma"), ("Merch_Gamma", "User_9921")
        ]
        theta = np.linspace(0, 2 * np.pi, len(nodes), endpoint=False)
        pos_x, pos_y = np.cos(theta), np.sin(theta)
        edge_traces_x, edge_traces_y = [], []
        for u, v in edges:
            i1, i2 = nodes.index(u), nodes.index(v)
            edge_traces_x.extend([pos_x[i1], pos_x[i2], None])
            edge_traces_y.extend([pos_y[i1], pos_y[i2], None])
            
        fig_network = go.Figure()
        fig_network.add_trace(go.Scatter(x=edge_traces_x, y=edge_traces_y, mode='lines', line=dict(width=2, color='rgba(239, 68, 68, 0.7)'), hoverinfo='none'))
        colors = ['#38bdf8' if 'User' in n else '#f59e0b' for n in nodes]
        fig_network.add_trace(go.Scatter(x=pos_x, y=pos_y, mode='markers+text', text=nodes, textposition="top center", marker=dict(size=30, color=colors, line=dict(width=2, color='#ffffff')), hoverinfo='text'))
        fig_network.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False), yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), height=480)
        st.plotly_chart(fig_network, use_container_width=True)
        
    with g_col2:
        st.markdown("#### 🚨 Isolated Ring Clusters")
        st.markdown("""
        <div style="background: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.3); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
            <b style="color: #f87171;">Ring Alpha (Hospitality Pass-Through)</b><br>
            <small><code>User_9921 → Merch_Alpha → User_4412 → User_9921</code></small><br>
            <b>Flow Symmetry</b>: CV 0.08 | <b>Cycle Time</b>: 42s<br>
            <b>Status</b>: <span style="color: #f87171;">Flagged for Freezing</span>
        </div>
        <div style="background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.3); border-radius: 8px; padding: 14px;">
            <b style="color: #fbbf24;">Ring Beta (Digital Micro-Smurfing)</b><br>
            <small><code>User_8819 → Merch_Beta → User_5501 → User_8819</code></small><br>
            <b>Flow Symmetry</b>: CV 0.11 | <b>Cycle Time</b>: 88s<br>
            <b>Status</b>: <span style="color: #fbbf24;">Rate Limits Active</span>
        </div>
        """, unsafe_allow_html=True)

with tab_kyc:
    st.markdown("### 🪪 Identity Integrity & OCR Repair Ledger")
    st.caption("Remediation of scanned identity cards and synthetic profile detection")
    col_k1, col_k2, col_k3 = st.columns(3)
    col_k1.metric("Ingested KYC Records", "36,400", "Master verification")
    col_k2.metric("OCR Confusions Fixed", "1,312", "92.4% recovery rate")
    col_k3.metric("Synthetic Flags", "108", "Multiple VPAs linked")
    kyc_sample = pd.DataFrame({
        "User ID": ["USR_1091", "USR_2412", "USR_8821", "USR_3319", "USR_9941"],
        "Tax Identifier (PAN)": ["ABCDE1234F", "XYZPA9912K", "MNBVC5541L", "QWERT8821P", "LKJHG4412M"],
        "Repair Status": ["Syntax Valid", "OCR Fixed (O→0)", "OCR Fixed (I→1)", "Syntax Valid", "Multi-Device Anomaly"],
        "Synthetic Risk": ["Low", "Low", "Medium", "Low", "Critical"]
    })
    st.dataframe(kyc_sample, use_container_width=True, hide_index=True)

with tab_agent:
    st.markdown("### 🤖 AgentIQ Natural Language Payment Analyst")
    st.caption("AI copilot translating queries into charts (Bar, Line, Scatter, Donut) and analytical briefings")

    # Initialize the Agent engine
    agent = AgentIQEngine(df)

    st.markdown("**Suggested Investigations (Click to load):**")
    q_col1, q_col2 = st.columns(2)
    with q_col1:
        if st.button("📌 Which merchant category has the highest chargeback-to-transaction ratio this quarter?"):
            st.session_state['agent_query'] = "Which merchant category has the highest chargeback-to-transaction ratio this quarter?"
    with q_col2:
        if st.button("📌 Show daily dispute trend over time"):
            st.session_state['agent_query'] = "Show daily dispute trend over time"

    user_query = st.text_input(
        "Enter analytical inquiry:",
        value=st.session_state.get('agent_query', "Which merchant category has the highest chargeback-to-transaction ratio this quarter?")
    )

    if st.button("Execute Agent Analysis", type="primary"):
        with st.spinner("Analyzing intent and rendering chart..."):
            fig, summary, chart_type = agent.generate_response(user_query)
            st.success(f"Visualization Selected: `{chart_type.upper()} CHART`")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(summary)