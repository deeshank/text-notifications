FROM python:3.4.5-slim

RUN pip install -U pip

RUN mkdir -p /opt/text-notifications
WORKDIR /opt/text-notifications

COPY . .

RUN pip install -r requirements.txt

ENV TWILIO_ACCOUNT_SID=
ENV TWILIO_AUTH_TOKEN=

EXPOSE 5000

CMD ["python", "manage.py", "runserver"]
