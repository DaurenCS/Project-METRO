# Use a lightweight base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose the port used by Telegram Bot API (optional)
EXPOSE 5432  

# Run the main script
CMD [ "python", "Bot.py" ]