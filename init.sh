udo rm -f /etc/nginx/sites-enabled/default

#sudo kill `pidof python`

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf

sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/test

sudo /etc/init.d/gunicorn restart

#gunicorn -D -b 0.0.0.0:8080 --workers=2 hello:app
