FROM python:3.6
RUN apt-get update && apt-get -y install \
    libpq-dev
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD ./reqs/requirements.txt /code/
ADD . /code/
RUN pip install -r requirements.txt
