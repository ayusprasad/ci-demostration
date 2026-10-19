# Power Calculator

[![CI](https://github.com/ayusprasad/ci-demostration/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/ci-demostration/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20demo-FF4B4B?logo=streamlit&logoColor=white)

A small Streamlit calculator that shows the square, cube, and fifth power of an integer.

## Features

- Interactive power calculator in a lightweight Streamlit interface.
- Pure calculation function with unit tests.
- GitHub Actions checks lint, tests, and compilation.

## Run locally

### Prerequisites

- Python 3.11 or newer

### Install and start

~~~bash
git clone https://github.com/ayusprasad/ci-demostration.git
cd ci-demostration
python -m venv .venv
~~~

Activate the environment (source .venv/bin/activate on macOS/Linux or .venv/Scripts/Activate.ps1 in PowerShell), then:

~~~bash
python -m pip install -r requirements.txt
streamlit run app.py
~~~

Open the local Streamlit URL shown in the terminal.

## Quality checks

~~~bash
ruff check --select E4,E7,E9,F app.py tests
pytest -q
~~~

No environment variables or external services are required.
