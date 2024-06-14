# syntax=docker/dockerfile:1.3-labs
FROM python:3.12.3

EXPOSE 80

WORKDIR /app/

RUN curl -sL https://deb.nodesource.com/setup_22.x | bash - && apt install -y nodejs

RUN pip install --upgrade pip poetry==1.8.3
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction

COPY . /app/

RUN <<EOF
set -e
export DJANGO_SETTINGS_MODULE=sample_deployment.settings
export DATABASE_URL=postgres://postgres:5432/postgres
export DJANGO_SECRET_KEY=secret

./manage.py tailwind install --no-input
./manage.py tailwind build --no-input
./manage.py collectstatic --no-input
EOF

CMD gunicorn -b 0.0.0.0:80 sample_deployment.wsgi --timeout 90 --workers 2 --threads 2
