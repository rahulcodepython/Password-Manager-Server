# Use a alpine Python base image for better performance
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Install system dependencies (e.g., for PostgreSQL)
# RUN apt-get update && apt-get install -y \
#     gcc \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy Django project files
COPY . .

# Expose the Django app port
# EXPOSE 8000

# Run Django server (modify for production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi:application"]