#!/bin/bash
sudo /etc/init.d/mysql start
sudo ./create_db.sh
sudo ./create_db_user.sh
python ./ask/manage.py syncdb
