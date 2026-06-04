import sys
import json
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def analyze_conflict_impact(conflicts, symbols):
    results = {}

    for symbol in symbols:
        # Fetch broad data range
        df = yf.download(symbol, start="2022-01-01", end="2026-06-03", progress=False)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        symbol_impacts = []
        for conflict_name, start_date in conflicts.items():
            start_ts = pd.to_datetime(start_date)
            end_ts = start_ts + timedelta(days=30)

            # Get closest available trading days
            mask = (df.index >= start_ts) & (df.index <= end_ts)
            conflict_period = df.loc[mask]

            if not conflict_period.empty:
                entry_price = float(conflict_period['Close'].iloc[0])
                exit_price = float(conflict_period['Close'].iloc[-1])
                return_pct = (exit_price - entry_price) / entry_price * 100

                symbol_impacts.append({
                    "conflict": conflict_name,
                    "start_date": start_date,
                    "entry_price": round(entry_price, 2),
                    "exit_price": round(exit_price, 2),
                    "return_30d_pct": round(return_pct, 2)
                })

        results[symbol] = symbol_impacts

    return results

if __name__ == "__main__":
    # Key geopolitical events 2022-2024
    major_conflicts = {
        "Ukraine Invasion": "2022-02-24",
        "Israel-Hamas Conflict": "2023-10-07",
        "Red Sea Crisis Escalation": "2024-01-12",
        "Iran-Israel Clash (Recent)": "2026-06-03" # From news data
    }

    target_symbols = ["GLD", "LMT"]

    analysis = analyze_conflict_impact(major_conflicts, target_symbols)
    print(json.dumps(analysis, indent=2))
