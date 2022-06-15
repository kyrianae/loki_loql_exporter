FROM debian:latest


COPY python/loki_logql_exporter/requirements.txt /requirements.txt

RUN apt update 
RUN apt install -y python3 python3-pip
RUN python3 -m pip install -r /requirements.txt

COPY python/loki_logql_exporter /loki_logql_exporter
WORKDIR /loki_logql_exporter
CMD python3 test_loki.py 
