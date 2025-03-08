# Python docker
FROM python:3.12-slim

# Install pip and poetry
RUN python -m pip install --upgrade pip
RUN pip install poetry

# Create the app directory
RUN mkdir /app

# Copy all files from the current directory to /app
COPY . /app

# Set /app as the working directory
WORKDIR /app

# Poetry run
RUN poetry install

# Entry point
ENTRYPOINT ["poetry","run", "run-agents"]