#!/bin/bash
sudo mysql -uroot -e "CREATE USER 'qa'@'localhost' IDENTIFIED BY 'qa'"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'qa'@'localhost'"
sudo mysql -uroot -e "FLUSH PRIVILEGES"
