# 🔄 Continuous Integration (CI) Demonstration

A hands-on demonstration of automated Continuous Integration workflows using **GitHub Actions**, **Pytest**, **Streamlit**, and **Docker**.

---

## 🌟 Highlights
- **Automated CI Pipeline:** On every push or pull request to `main`, GitHub Actions automatically checks out the repository, installs dependencies, and runs the Pytest verification suite.
- **Modern Action Runners:** Upgraded to `actions/checkout@v4` and `actions/setup-python@v5`.
- **Modular Codebase:** Production calculations separated into `math_utils.py`, tested by `_test.py`, and visualized by `app.py`.
- **Container Build Test:** Docker build runs tests automatically before container packaging.

---

## 🚀 Quickstart

### 1. Run Tests Locally
```bash
pip install -r requirements.txt
pytest _test.py -v
```

### 2. Run Streamlit App
```bash
streamlit run app.py
```

### 3. Run with Docker
```bash
docker build -t ci-demo .
docker run -p 8501:8501 ci-demo
```
Open [http://localhost:8501](http://localhost:8501).