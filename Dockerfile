From python:3.5

WORKDIR /app
COPY ./app /app
ENV FLASK_APP hello.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["flask", "run"]
