# Stage 1: Prepare backend package dependencies
FROM python:3.11-alpine AS builder

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    python3-dev

# Copy requirements
COPY backend/requirements.txt .

# Install Python dependencies into /install
RUN pip install --prefix=/install -r requirements.txt

# Copy backend code
COPY backend/ .

# ------------------------------
# Stage 2: Final Runtime Image
# ------------------------------
FROM python:3.11-alpine

WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /install /usr/local

# Copy backend code
COPY backend/ .

# Copy frontend
COPY frontend/ /app/frontend/

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

