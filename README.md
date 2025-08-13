FScienceCheck - science project for reading science literature
=========================

This application was made for people, who don't want interact the complex interface and a lot of settings. FScienceCheck made in minimalizm and give to a user important information, if user want to explore more he can go on more powerfull libraries.

* This is a pet project
* Application gives Django interface to add examples of science works, not API
* FScienceCheck adaptive for web-view and android

# How to use local version
Code bellow in that conditions can run in 2 situations:

* Localhost run
* Server production run

For run in Localhost you need install Python version 3.10 +


So after that starts the Django activation. You could find it in the internet if you don't now how to deal with.

To run application you need create a .env.dev file: docker/env/.env.dev

```

SECRET_KEY=<djangokey>
DEBUG=1
ALLOWED_HOSTS=127.0.0.1 localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1 http://localhost
POSTGRES_DB=<dbName>
POSTGRES_USER=<dbUser>
POSTGRES_PASSWORD=<dbPassword>
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

```
And if you dont't know russian swap language in settings.

For local run you should comment certbot container in compose file

```
#  certbot:
#      image: certbot/certbot
#     container_name: certbot
#      volumes:
#          - ./docker/certbot/conf:/etc/letsencrypt:rw
#          - ./docker/certbot/www:/var/www/certbot:rw
#      command: certonly --webroot --webroot-path=/var/www/certbot/ --email <your email> --agree-tos --no-eff-email -d <domain name> -d www.<domain name> && 2 <uncomment for reaching certificate>
#      depends_on:
#        - nginx
```
And also litte rewrtire nginx container

```
  nginx:
    container_name: nginx
    working_dir: /API_science
    image: nginx:stable-alpine
    restart: always
    ports:
      - "80:80"
    volumes:
      - static:/app/static
      - ./docker/nginx/dev/:/etc/nginx/conf.d:ro
    links:
      - django
    depends_on:
      - django
```
And also change in django container .prod to .dev and change line ```` gunicorn --workers=4 --reload --max-requests=1000 API_science.wsgi -b 0.0.0.0:8000" ```` to ````python manage.py runserver 0.0.0.0:8000" ````

After that you can create container for app and run it and enjoy application. If you want to add some works, create a superuser.

# How to use production version


Rewrite nginx file in: /docker/nginx/django.conf
With  code in:
```
upstream django {
    server django:8000;
}

server {
    listen 80;
    listen [::]:80;

    server_name fsciencecheck;
    server_tokens off;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}


# server {
#     listen 443 default_server ssl http2;
#     listen [::]:443 http2;
#
#     server_name <domain like smt.com>;
#     server_tokens off;
#
#     ssl_certificate /etc/letsencrypt/live/<domain name>/fullchain.pem;
#     ssl_certificate_key /etc/letsencrypt/live/<domain name>/privkey.pem;
#
#
#     client_max_body_size 20M;
#     charset utf-8;
#
#     gzip  on;
#     gzip_disable "msie6";
#     gzip_min_length 1000;
#     gzip_vary on;
#     gzip_proxied   expired no-cache no-store private auth;
#     gzip_types     text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/javascript;
#
#     location / {
#         proxy_set_header X-Forwarded-Proto https;
#         proxy_set_header X-Url-Scheme $scheme;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header Host $http_host;
#         proxy_redirect off;
#         proxy_pass http://django;
#     }
#
#     location /static/ {
#         alias  /API_science/static/;
#         expires 15d;
#     }
#
#     if ($http_host !~ "^<domain name>$"){
#            rewrite ^(.*)$ <domain name>$1 redirect;
#        }
# }
```

Second server part commented due to getting SSL certificate. After getting certificate you should uncomment this.

After creating nginx file let's create docker-compose file

```
volumes:
  pgdata:
  static:


services:

  django:
    build:
      context: .
      network: host
    ports:
      - '8000:8000'
    container_name: django
    env_file:
      - docker/env/.env.prod
    volumes:
      - ./:/API_science
      - static:/API_science/static
    depends_on:
      - postgres
    command: sh -c "python manage.py makemigrations &&
                    python manage.py migrate &&
                    python manage.py loaddata fixtures/people.json && # You can and fixtures, if you want
                    python manage.py loaddata fixtures/types.json &&
                    python manage.py loaddata fixtures/AllUnion.json &&
                    gunicorn --workers=4 --reload --max-requests=1000 API_science.wsgi -b 0.0.0.0:8000"

  nginx:
    container_name: nginxTest
    working_dir: /API_science
    image: nginx:stable-alpine
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - static:/API_science/static
      - ./docker/nginx/:/etc/nginx/conf.d:ro
      - ./docker/nginx/prod/:/etc/nginx/conf.d:ro
      - ./docker/certbot/conf:/etc/letsencrypt:ro
      - ./docker/certbot/www:/var/www/certbot:ro
    links:
      - django
    depends_on:
      - django

  postgres:
    image: postgres:alpine
    container_name: postgresTest
    restart: always
    env_file:
      - docker/env/.env.prod
    volumes:
      - pgdata:/var/lib/postgresql/data/

  certbot:
      image: certbot/certbot
      container_name: certbot
      volumes:
          - ./docker/certbot/conf:/etc/letsencrypt:rw
          - ./docker/certbot/www:/var/www/certbot:rw
#      command: certonly --webroot --webroot-path=/var/www/certbot/ --email <your email> --agree-tos --no-eff-email -d <domain name> -d www.<domain name> && 2 <uncomment for reaching certificate>
      depends_on:
        - nginx
```

After this mannipulation you need upload this to server.
In console:
* Download docker and docker-compose
* docker-compose build
* docker compose up nginx certbot
* docker compose stop
* Comment line of code with certbot
* Uncomment remain nginx file
* docker-compose build
* docker-compose up
