FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV FLASK_DEBUG false
ENV FLASK_APP /code/app

WORKDIR /code
COPY /src /code

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

EXPOSE 8000

ENTRYPOINT flask run -h 0.0.0.0 -p $PORT
