# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app will run on (if you're using Flask)
EXPOSE 5000

# Define environment variable
ENV NAME ScamEye-Model

# Run app.py when the container launches
CMD ["python", "app.py"] # or your main python file