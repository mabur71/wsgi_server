#!/bin/bash

#/etc/nginx/nginx.conf - config nginx

sudo rm -f /etc/nginx/sites-enabled/default

#sudo kill `pidof python`

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf

sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.test.conf   /etc/gunicorn.d/test

sudo ln -sf /home/box/web/etc/gunicorn.ask.conf   /etc/gunicorn.d/ask

sudo /etc/init.d/gunicorn restart

#gunicorn -D -b 0.0.0.0:8080 --workers=2 hello:app
