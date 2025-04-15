# Base Image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Expose port for FastAPI app
EXPOSE 80

# Command to run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
