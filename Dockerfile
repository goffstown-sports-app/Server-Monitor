# Base image
FROM python:3.6-stretch

# Meta for Docker Hub
LABEL description="📂 Keeps an eye on the server. If something looks weird all maintainers get sent an email"
LABEL maintainer="matthewgleich@gmail.com"

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Depencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copying over files
COPY /src /src
RUN rm -f /src/firestore_creds.json
WORKDIR /src

# Running program
CMD ["python3", "main.py"]
