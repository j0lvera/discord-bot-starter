# Discord Bot starter

This is a simple Discord bot written in Python that uses the Discord.py library to interact with the Discord API. The bot is containerized using Docker, making it easy to deploy and run on any system with Docker installed.

## Prerequisites

Before you can run the bot, you need to have the following installed on your system:

- Docker
- Python 3.6 or higher
- Poetry 

## Getting Started

To get started with the bot, follow these steps:

```bash
# Install dependencies
poetry install
```

```bash
# Run the bot locally
poetry run python run.py
```

```bash
# Generate the requirements.txt file
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

```bash
# Build the Docker image
docker build -t discord-bot .
```

```bash
# Run the Docker container
docker run -d --name discord-bot discord-bot
```

```bash
# Or using docker-compose
docker-compose up -f docker/docker-compose.yml up -d
```