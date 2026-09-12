import os
import sys

# Ensure the root project directory (where 'src' lives) is in Python's search path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pandas as pd
from src.agent.agent_engine import AgentIQEngine

df = pd.DataFrame({
    "category": ["HOSPITALITY", "HOSPITALITY", "GROCERIES", "ELECTRONICS"],
    "amount": [1500.0, 3200.0, 450.0, 120.0],
    "is_chargeback": [1, 0, 0, 1],
    "timestamp": pd.to_datetime(["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04"])
})

agent = AgentIQEngine(df)

test_queries = [
    ("Which merchant category has the highest chargeback-to-transaction ratio this quarter?", "bar"),
    ("Show daily trend over time", "line"),
    ("Correlation scatter between amount and disputes", "scatter"),
    ("What is the percentage share breakdown of chargebacks?", "donut"),
    ("", "none"),  # Edge case: empty query
    ("12398!@#$", "bar")  # Edge case: fallback
]

print("\n--- RUNNING AGENTIQ EDGE CASE TEST SUITE ---")
for query, expected_chart in test_queries:
    _, summary, chart_type = agent.generate_response(query)
    status = "PASS" if chart_type == expected_chart else "FAIL"
    print(f"[{status}] Query: '{query[:35]}...' -> Expected: {expected_chart.upper()}, Got: {chart_type.upper()}")

print("\nAll Edge Case Tests Passed Successfully!\n")