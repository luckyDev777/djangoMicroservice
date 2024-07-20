FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE user_service.settings

WORKDIR /app

COPY post_requirements.txt /app/
RUN pip install --no-cache-dir -r post_requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
