# SmartShop — AI Grocery & Meal Planner Agent

SmartShop is a multi-agent Concierge system that automates weekly meal planning, pantry-aware grocery lists,
and cost estimation. This repository contains a modular skeleton implementation suitable for demonstration
and extension for the Kaggle Agents Intensive - Capstone Project.

## Features
- Planner Agent (orchestrator)
- Recipe Research Agent (mocked dataset)
- Shopping Optimizer Agent (grocery list grouping & cost estimation)
- Pantry Tool (ingredient normalization & missing items computation)
- Memory Bank (simple JSON-based long-term memory)
- Demo script to run a sample planning session

## How to run (local)
1. Clone the repo
2. `python3 -m venv venv && source venv/bin/activate` (or use conda)
3. `pip install -r requirements.txt`
4. `python smartshop/main.py`

## Notes
- This is a demo skeleton. External APIs are mocked or optional.
- Do NOT commit API keys. Use environment variables for credentials if you integrate live services.
