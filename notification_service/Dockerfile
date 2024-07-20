# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE user_service.settings

# Create and set the working directory
WORKDIR /app

# Install dependencies
COPY notification_requirements.txt /app/
RUN pip install --no-cache-dir -r notification_requirements.txt

# Copy the project files
COPY . /app/

# Copy the start script
COPY start.sh /app/start.sh

# Make the start script executable
RUN chmod +x /app/start.sh

# Expose the port the app runs on
EXPOSE 8000

# Run the start script
CMD ["/app/start.sh"]
