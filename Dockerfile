# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary packages and Chrome
#RUN apt-get update && apt-get install -y wget curl unzip && apt-get install -y gnupg2

# Install Chrome
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
#RUN apt-get update && apt-get install -y google-chrome-stable

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your Selenium test script into the container
COPY test_script.py .

# Command to run the Selenium test script
CMD ["python3", "test_script.py"]
