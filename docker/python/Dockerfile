FROM python:3.6
MAINTAINER daru015@gmail.com

COPY ./src /src

WORKDIR /src

RUN pip install -r requirements.txt

COPY ./docker/python/start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]
