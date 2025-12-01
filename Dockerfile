FROM python:3.10-slim

WORKDIR /app

# Copy backend
COPY backend ./backend

# Copy frontend
COPY frontend ./frontend

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 9000

# Run server
CMD ["python", "backend/app.py"]
