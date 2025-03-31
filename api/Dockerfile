# Use an official Python runtime as a base image
FROM python:3.12-slim

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . . 

# Run your application
CMD ["python", "./main.py"]
