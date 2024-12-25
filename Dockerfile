# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /fwdbot

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the working directory
COPY . .

# Ensure that start.sh is executable
RUN chmod +x start.sh

# Command to run the bot when the container starts
CMD ["python", "bot.py"]
