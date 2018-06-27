FROM python:3.7.0b2-stretch

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY metadatacreator/* /usr/src/app/metadatacreator/
COPY __init__.py /usr/src/app/

WORKDIR /usr/src/app

