FROM python:3.10

RUN apt-get update -y
RUN apt-get install -y iputils-ping
COPY ./discover_mtu.py /

ENTRYPOINT ["python3", "/discover_mtu.py"]
