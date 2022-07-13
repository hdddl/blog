# syntax=docker/dockerfile:1
FROM python:3.8.13

# update the os
RUN apt-get -y update
RUN apt-get -y install pandoc
RUN apt-get -y install nginx

COPY script/blog.conf /etc/nginx/sites-enabled/default
COPY . /app

WORKDIR /app
RUN pip install --root-user-action=ignore -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:13248"]
