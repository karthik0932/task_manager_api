# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose Django port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]