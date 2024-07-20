FROM python:3.11-slim


ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE user_service.settings


WORKDIR /app

COPY notification_requirements.txt /app/
RUN pip install --no-cache-dir -r notification_requirements.txt

COPY . /app/

COPY wait-for-it.sh /app/wait-for-it.sh
COPY start.sh /app/start.sh

RUN chmod +x /app/start.sh

RUN chmod +x /app/wait-for-it.sh /app/start.sh

EXPOSE 8000

CMD ["/app/start.sh"]
