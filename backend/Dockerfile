# Use an official lightweight Python image
FROM python:3.11-slim

# Set system environment variables to optimize Python inside Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for compilation if any
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy just the requirements first to leverage Docker's caching layer
COPY requirements.txt .

# Install dependencies directly into the container system
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and model artifacts
COPY ./app ./app
COPY ./models ./models

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]