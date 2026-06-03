# Jules + FinceptTerminal: The AI Engineering Partner Guide

Welcome to the documentation for **Jules**, your extremely skilled software engineer and AI partner integrated into **FinceptTerminal**. This guide explains how to use Jules effectively for trading, research, and expanding the terminal's capabilities.

---

## 1. Architecture Overview

FinceptTerminal is a native C++20/Qt6 application. Jules interacts with it through the **Model Context Protocol (MCP)**.

-   **C++ Core**: Handles high-performance UI, rendering, and the DataHub pub/sub system.
-   **MCP Bridge**: Translates LLM (Large Language Model) tool calls into C++ actions or Python script executions.
-   **Jules (AI)**: Resides in the AI Chat and can see the terminal's state, call data tools, and even modify the codebase.

---

## 2. Core Integration: The MCP Bridge

Jules has access to 24+ tool modules. Every action you see in the terminal—fetching a quote, placing a trade, or generating an AI Quant Lab model—can be performed by Jules.

### Key Tool Categories:
-   **Markets**: `markets.get_quote`, `markets.get_historical`.
-   **DataHub**: `datahub_peek`, `datahub_subscribe_briefly` (see `datahub-guide.md`).
-   **Trading**: `paper.place_order`, `broker.get_positions`.
-   **AI Quant Lab**: `quant.generate_factor`, `quant.backtest_strategy`.

---

## 3. How to Use Jules (User Guide)

### For Research and Analysis
Ask Jules to analyze an asset. Jules can fetch data, look at news sentiment, and provide a technical forecast.
*   *Example:* "Analyze BTC-USD on the 4H timeframe and give me a forecast."

### For AI Quant Lab
Jules can help you discover new alpha factors and backtest them.
*   *Example:* "Create a momentum-based factor for the Nifty 50 and run a 1-year backtest."

### For Engineering
Since Jules is an engineer, you can ask to modify the terminal itself.
*   *Example:* "Add a new data connector for the Federal Reserve API in `scripts/fred_data.py`."

---

## 4. Инструкция для пользователя (Russian)

### Как пользоваться Jules в связке с FinceptTerminal

Jules — это ваш ИИ-партнер, встроенный прямо в терминал. Он понимает команды на русском и может управлять функциями программы.

**Основные возможности:**
1.  **Трейдинг:** Вы можете попросить: "Купи 1 BTC на бумажном счете" или "Покажи мои текущие позиции".
2.  **Аналитика:** Спросите: "Дай прогноз по акциям Apple на основе последних новостей". Jules изучит график и ленту новостей.
3.  **AI Quant Lab:** Jules может писать код для ваших торговых стратегий. "Напиши фактор на основе RSI и проверь его прибыльность за прошлый год".
4.  **Мониторинг:** Используйте DataHub для слежки за рынком в реальном времени. "Следи за ценой ETH 5 секунд и скажи, есть ли волатильность".

**Как вызвать инструмент:**
Просто опишите задачу в AI Chat. Jules сам выберет нужный инструмент (MCP Tool) и выполнит его.

---

## 5. For Developers: Adding New Tools

To add a tool that Jules can use:
1.  **Script**: Add your Python logic in `fincept-qt/scripts/`.
2.  **Schema**: Define the tool schema in `src/mcp/tools/`.
3.  **Handler**: Register the async handler in `McpProvider.cpp` to call your script.

Refer to `MCP_TOOLS_GUIDE.md` for the full technical walkthrough.

---

## 6. Diagnosis and Help

If Jules cannot find a tool:
-   Run `mcp.health` in the chat.
-   Check if the tool is registered in `McpInit.cpp`.
-   Ensure the Python environment is active (`agno` and `yfinance` installed).

---
*Fincept Corporation © 2026*
