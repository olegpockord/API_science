FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


CMD ["--network","host"]


RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev


RUN pip install --upgrade pip


COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

WORKDIR /API_science


RUN apk del .build-deps


COPY . .


RUN chmod -R 777 ./