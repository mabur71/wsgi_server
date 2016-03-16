sudo rm -f /etc/nginx/sites-enabled/default
#sudo kill `pidof python`
sudo ln -sf /home/`echo $USER`/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/`echo $USER`/web/etc/gunicorn.test.conf   /etc/gunicorn.d/test
sudo ln -sf /home/`echo $USER`/web/etc/gunicorn.ask.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
#gunicorn -D -b 0.0.0.0:8080 --workers=2 hello:app


