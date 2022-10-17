FROM python:3.8.3-slim 

WORKDIR /PY

COPY ./ ./

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

RUN pip3 install -r requirements.txt

CMD ["python3", "demo.py"]

EXPOSE 8080