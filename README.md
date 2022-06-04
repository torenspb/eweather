# About us
EWeather is an Estonian startup that provides the most important news. Weather news.  
This repository contains the MVP version of the project.

# How to run
You can use the pre-built docker container that contains the latest application version.  
Simply pull the container from the docker hub and run it:
```
docker pull spolikarpov/eweather:latest
docker run --rm --name eweather -p 80:80 spolikarpov/eweather:latest
```
You can also build a docker container and run it:
```
docker build -t eweather:local .
docker run --rm --name eweather -p 80:80 eweather:local
```
Or install the python requirements and run the app:
```
pip install -r requirements.txt
python app.py
```
