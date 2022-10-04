FROM python:3.9-slim

WORKDIR /app

RUN apt-get -qq update -y && apt-get --no-install-recommends -y install vim procps && apt-get -y install libpq-dev gcc
RUN pip install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 8000

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod a+x /app/deploy/docker_entrypoint.sh
ENTRYPOINT ["/app/deploy/docker_entrypoint.sh"]