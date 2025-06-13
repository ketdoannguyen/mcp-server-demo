# Multi-stage Dockerfile for MCP Server
# Stage 1: Builder
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

# Copy dependency files first for better caching
COPY pyproject.toml README.md ./
COPY uv.lock ./

# Copy source code
COPY src ./src

# Install dependencies with uv
RUN uv sync --frozen --no-dev --no-cache

# Stage 2: Production
FROM python:3.12-slim-bookworm AS production

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy application code and configuration
COPY --from=builder /app/src /app/src
COPY --from=builder /app/pyproject.toml /app/
COPY --from=builder /app/README.md /app/

# Ensure we use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/src"

# Environment variables
ENV HOST=0.0.0.0
ENV PORT=8000
ENV ENVIRONMENT=production
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose port
EXPOSE 8000

# Default command
CMD ["python", "src/mcp_server/server.py"]