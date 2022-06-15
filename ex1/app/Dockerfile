FROM python:3.9.6-slim-buster
#Simple image metadata containing tags such as author, description, etc.
LABEL author="Douglas F. Neves <douglasfneves@gmail.com>" \
      app="GetWeather" \
      description="Gets current weather from https://openweathermap.org/api" \
      version="v1.0"
#Creates a directory and cd's into it
WORKDIR /app
#Copies everything in the Dockerfile folder to target folder (in container)
COPY . /app
# -U: updates PIP version
# -r = requirements
# Any and all python libraries that are deemed necessary can be entered into requirements.txt
RUN python3 -m pip install -U pip && python3 -m pip install -r requirements.txt
#This command ensures everything will be run as a non-privileged userID (First 999 users are privileged)
USER 1001

ADD webxshieldx

#The very first thing the container will do upon activation
ENTRYPOINT ["/app/getweather"]
