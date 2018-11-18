FROM python:3.6
MAINTAINER daru015@gmail.com

COPY ./src /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
