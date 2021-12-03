FROM python:3.10

ENV DJANGO_SETTINGS_MODULE=liska.settings

WORKDIR /app
COPY requirements.txt ./
EXPOSE 8088

RUN apt update && \
    pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY . ./

ENV PACKAGE_VERSION=$package_version
RUN useradd -M app
# RUN useradd -M app && DATABASE_URL="sqlite:///db" ./manage.py collectstatic --no-input && chown -R app:app /app
USER app

# CMD [ "gunicorn", "--bind", ":8000", "--worker-class", "gevent", "--access-logfile", "-", "boocsek.wsgi:application" ]
