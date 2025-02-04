# Base image
FROM python:3.6-stretch

# Meta for Docker Hub
LABEL author matthewgleich@gmail.com

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Depencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copying over files
COPY /serverMonitor /serverMonitor
RUN find . -name \*.json -type f -delete
WORKDIR /serverMonitor

# Running program
CMD ["python3", "main.py"]
