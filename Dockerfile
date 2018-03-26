FROM python:3.4.5-slim

RUN pip install -U pip

RUN mkdir -p /opt/text-notifications
WORKDIR /opt/text-notifications

COPY . .

RUN pip install -r requirements.txt

ENV TWILIO_ACCOUNT_SID=AC40fa910e33465a80684c0f4ce40e759d
ENV TWILIO_AUTH_TOKEN=098f11c167c5fd89736a4307aaa4ec79

EXPOSE 5000

CMD ["python", "manage.py", "runserver"]
