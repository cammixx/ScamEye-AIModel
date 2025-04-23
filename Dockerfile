# Dockerfile
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy files
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . /app

# Expose FastAPI port
EXPOSE 8000

# Start the app
CMD ["bash", "uvicorn_start.sh"]
