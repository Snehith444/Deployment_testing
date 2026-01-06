FROM python:3.12-slim

# Project root inside container
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the app package
COPY app/ app/

# Make /code visible to Python imports
ENV PYTHONPATH=/code

# Expose port
EXPOSE 8000

# Run FastAPI (NO reload in Docker)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
