# Base image
FROM python:3.11-slim

# Working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose FastAPI port
EXPOSE 80

# Run FastAPI App
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
