# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY . /app/

# Set environment variables
ARG HOST
ARG PORT
ENV HOST=${HOST}
ENV PORT=${PORT}

# Expose the port on which the FastAPI server will run (change as needed)
EXPOSE ${PORT}

# Command to run the FastAPI server
CMD ["sh", "-c", "uvicorn api:app --host $HOST --port $PORT"]
