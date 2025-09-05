FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies with cache mounting for better performance
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Enable bytecode compilation for better performance
ENV PYTHONOPTIMIZE=1
ENV PYTHONUNBUFFERED=1

# Set transport and port environment variables
ENV TRANSPORT=http
ENV PORT=8000

# Expose the port
EXPOSE 8000

# Run the server
CMD ["python", "server.py"]
