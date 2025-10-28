# StockSmart Backend

This directory contains a minimal FastAPI backend scaffold for the StockSmart project.

Structure:
- app/: FastAPI application package
- requirements.txt: Python dependencies
- .env: local environment variables

To run locally (after installing dependencies):

1. python -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. uvicorn app.main:app --reload
