FROM python:3.6-stretch

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


COPY dev-requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY /serverMonitor /serverMonitor
COPY /tests /tests

WORKDIR /tests
CMD ["pytest", "--emoji"]
