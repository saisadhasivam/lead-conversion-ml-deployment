FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY final_lead_conversion_model.pkl .
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
