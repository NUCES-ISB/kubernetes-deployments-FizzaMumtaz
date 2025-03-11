# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files from the `app/` folder
COPY app/requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app/ .

# Expose the port Flask runs on
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
