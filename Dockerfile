# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY . .

# Default command
CMD ["pytest", "-q"]
