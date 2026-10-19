FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run automated tests during container build
RUN pytest _test.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
