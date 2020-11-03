FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends vim

RUN pip install Mako

RUN pip install matplotlib

RUN mkdir -p /sitespeed.io/report

WORKDIR /sitespeed.io

COPY script.py .
COPY info.py .
COPY detailed.py .
COPY detailed_parallels_runs.py .
COPY graphs.py .
COPY graphs.sh .
COPY diff.py .
COPY diff.sh .
COPY diff_parallels_runs.sh .
COPY diff_parallels_runs.py .
COPY lighthouse.py .
COPY lighthouse_a.py .
COPY lighthouse.sh .
COPY lighthouse_a.sh .
COPY common_report.sh .
COPY common_report_parallel.sh .
COPY html html

ENTRYPOINT ["./common_report.sh"]
