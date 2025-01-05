FROM --platform=linux/amd64 python:3.10.2-slim AS app

# Send python output to terminal (standard output) without buffering.
ENV PYTHONBUFFERED 1

# Prevent python from writing pyc files to disc.
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory for the application
WORKDIR /app

# Define build arguments for user and group IDs
ARG UID=1000
ARG GID=1000

# Install system dependencies, create user group and set permissions
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean \
    && groupadd -g $GID python \
    && useradd --create-home --no-log-init -u $UID -g $GID python \
    && chown python:python -R /app

# Switch to non-root user for security
USER python

# Copy requirements file with appropriate permissions
COPY --chown=python:python requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set environment variables for Python path, system PATH, and user
ENV PYTHONPATH="." \
    PATH="/usr/local/bin:/home/python/.local/bin:${PATH}" \
    USER="python"

# Copy application code and set appropriate permissions
COPY --chown=python:python .. /app

# Define the command to run the application
CMD [ "python", "run.py" ]