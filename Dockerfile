# Use a lightweight Python base image
FROM python:3.10.13-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt update -qq && \
    apt install -y --no-install-recommends git ffmpeg && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Create app directory and set permissions
WORKDIR /app
COPY . /app
RUN chmod +x bash.sh

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Expose port for health check (Flask or other)
EXPOSE 8080

# Start the bot
CMD ["bash", "bash.sh"]
