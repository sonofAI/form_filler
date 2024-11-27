FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default command (will be overridden by Docker Compose)
CMD ["python", "main.py"]
