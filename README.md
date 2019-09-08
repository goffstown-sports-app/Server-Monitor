# Server-Monitor

## Services

| Service Name | Badge                                                                                                                                                                                                                                                                                           | Description                   |
|-------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Synk         | [![Known Vulnerabilities](https://snyk.io/test/github/goffstown-sports-app/Server-Monitor/badge.svg)](https://snyk.io/test/github/goffstown-sports-app/Server-Monitor)                                                                                                              | Security Monitoring           |
| Travis CI    | [![Build Status](https://travis-ci.com/goffstown-sports-app/Server-Monitor.svg?branch=master)](https://travis-ci.com/goffstown-sports-app/Server-Monitor)                                                                                                                           | Continous Integration Service |
| Codacy       | [![Codacy Badge](https://api.codacy.com/project/badge/Grade/79e012cb6bc4425ba829dd60aa517c87)](https://app.codacy.com/app/matthewgleich/Server-Monitor?utm_source=github.com&utm_medium=referral&utm_content=goffstown-sports-app/Server-Monitor&utm_campaign=Badge_Grade_Settings) | Cloud based linter            |

## Description

The server monitor application works off of database pulses. Each micro service sends a pulse to the database every time it runs. The server monitor application looks all the last pulse time for each micro service and checks the make sure it was updated on time. If it didn't update in time, then everyone on the email list will be notified.

## Features

Below is a list of all the features of this program:

1. Send email when program didn't update on time
2. Send email when program is back on time.
3. Set a status for each program based on if it running or not

## Requirements

To see working python version look at the .travis.yml

Install the requirements by doing the following:

`pip install -r requirements.txt`

## Usage

Once you have installed the requirements, you can now run the program! You run the program by inputting the following command once you are in the src folder:

`python main.py`

## Contributors

* [Matthew Gleich](https://github.com/Matt-Gleich) (@Matt-Gleich)
