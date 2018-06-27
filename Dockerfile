FROM python:3.7-rc-stretch

RUN apt-get update && apt-get install -y python3-numpy python3-pandas
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY metadatacreator/* /usr/src/app/metadatacreator/
COPY data/* /usr/src/app/data/
COPY __init__.py /usr/src/app/

WORKDIR /usr/src/app

