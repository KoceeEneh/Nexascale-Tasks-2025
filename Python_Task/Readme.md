# PYTHON TASK
## This repository contains three python projects
- Weather API Fetcher - Retrieves and displays weather details for a given city.

- CPU & Memory Monitor - Continuously monitors and logs system CPU and memory usage.

- System Log Scanner - Scans a log file for "ERROR" occurrences and filters logs by severity.
---

# 1. Weather API Fetcher

## Description
This script fetches the weather details (temperature, condition, and humidity) for a given city using the OpenWeather API.

## Requirments
- python 3
- `requests` library
- OpenWeather API key

## Setup
- Sign up at OpenWeatherMap to get a free API key.
- create a .env file and app your API key:

```bash
OPENWEATHER_API_KEY=your_api_key_here
```
- install dependencies:

```bash
pip install requests python-dotenv
```
- Run the script:

```bash
python3 weather_API.py
```

## output

```bash
Enter city name: Lagos
Weather in Lagos:
Temperature: 30°C
Condition: Clear sky
Humidity: 75%
```
--- 

# 2.CPU & Memory Monitor

## Description
This script monitors CPU and memory usage every few seconds and logs it to a file.

## Requirments
- python3
- psutil library

## Setup
- install psutil

```bash
pip install psutil
```

- run the script

```bash
python sys_Mon.py
```

- stop script with CTRL+C. this saves the log to a file.

## Output

```bash
Monitoring system... (Ctrl+C to stop)
CPU USAGE: 35%
MEMORY USAGE: 60%
```
---

# 3.System Log Scanner

## Description
This script scans a .log file, counts occurrences of the word "ERROR," and filters logs by severity level (INFO, WARNING, ERROR).

## Requirements
- Python3

## Setup
- Ensure a log file (demo.log) exists. If not, the script will create a sample one.

- run the script

```bash
python log.py
```

## output

```bash
Logs with 'ERROR':
ERROR - Database connection failed
ERROR - Timeout while fetching data
Found 2 occurrences of 'ERROR'.
Found 2 ERROR logs in 'demo.log'.
```








