FROM python:3.6

ENV FLASK_APP=main.py
ENV FLASK_CONFIG=development

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]