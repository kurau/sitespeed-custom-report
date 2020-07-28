FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends vim

RUN pip install Mako

RUN pip install matplotlib

RUN mkdir -p /sitespeed.io/report

WORKDIR /sitespeed.io

COPY script.py .
COPY info.py .
COPY detailed.py .
COPY graphs.py .
COPY graphs.sh .
COPY diff.py .
COPY diff.sh .
COPY lighthouse.py .
COPY lighthouse.sh .
COPY common_report.sh .
COPY html html

ENTRYPOINT ["./common_report.sh"]
