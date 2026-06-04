"""
Simple Backtest Example for Jules User Guide
Strategy: Buy if price grew 2% in a day, Sell if it fell 1% from entry.
"""

import sys
import json
import os
import pandas as pd
import yfinance as yf

def run_simple_backtest(symbol, start_date, end_date, capital=10000):
    # Fetch data
    df = yf.download(symbol, start=start_date, end=end_date, interval="1d", progress=False)
    if df.empty:
        return {"error": "No data found"}

    # Fix MultiIndex: (Price, Ticker) -> Price
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Initialize variables
    cash = capital
    position = 0
    entry_price = 0
    history = []

    # Iterate through days
    for i in range(1, len(df)):
        current_date = df.index[i].strftime("%Y-%m-%d")

        # Calculate 1-day return
        try:
            prev_close = float(df['Close'].iloc[i-1])
            curr_close = float(df['Close'].iloc[i])
        except (KeyError, IndexError, ValueError):
            continue

        daily_return = (curr_close - prev_close) / prev_close

        # Strategy Logic
        if position == 0:
            # Buy if grew 2%
            if daily_return >= 0.02:
                shares = cash / curr_close
                if shares > 0:
                    position = shares
                    entry_price = curr_close
                    cash = 0
                    history.append({"date": current_date, "action": "BUY", "price": round(entry_price, 2)})
        else:
            # Sell if fell 1% from entry
            exit_return = (curr_close - entry_price) / entry_price
            if exit_return <= -0.01:
                cash = position * curr_close
                history.append({"date": current_date, "action": "SELL", "price": round(curr_close, 2), "pnl_pct": round(exit_return * 100, 2)})
                position = 0
                entry_price = 0

    # Final valuation
    final_price = float(df['Close'].iloc[-1])
    total_value = cash + (position * final_price)
    total_return = (total_value - capital) / capital * 100

    return {
        "symbol": symbol,
        "initial_capital": capital,
        "final_value": round(total_value, 2),
        "total_return_pct": round(total_return, 2),
        "trades": history,
        "data_points": len(df)
    }

if __name__ == "__main__":
    sym = sys.argv[1] if len(sys.argv) > 1 else "BTC-USD"
    start = sys.argv[2] if len(sys.argv) > 2 else "2024-01-01"
    end = sys.argv[3] if len(sys.argv) > 3 else "2024-12-31"

    result = run_simple_backtest(sym, start, end)
    print(json.dumps(result, indent=2))
