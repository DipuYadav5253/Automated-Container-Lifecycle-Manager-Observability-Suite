# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy our worker script into the container
COPY worker.py .

# Run the worker
CMD ["python", "worker.py"]