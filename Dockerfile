FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Set default environment variables
ENV TRANSPORT=http
ENV PORT=8000

CMD ["python", "server.py"]
