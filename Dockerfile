FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends vim

RUN pip install Mako

RUN mkdir -p /sitespeed.io/report

WORKDIR /sitespeed.io

COPY script.py .
COPY template.html .
COPY detailed_template.html .
COPY help.html .
COPY index.min.css .

ENTRYPOINT ["python", "script.py"]
