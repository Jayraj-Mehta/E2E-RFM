# Use an official lightweight Python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app code
COPY app.py .

# Expose the default Streamlit port
EXPOSE 8501

# Command to run Streamlit with production flags
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]