#!/usr/bin/env bash
# Preparing my webservers with this script
sudo apt-get update

sudo apt-get install -y nginx

sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/

sudo mkdir -p /data/web_static/

sudo mkdir -p /data/web_static/releases/

sudo mkdir -p /data/web_static/shared/

sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html

# sudo mkdir -p /data/web_static/releases/test/

# sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

replace_str="server_name _;\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"

sudo sed -i "s/server_name _;/$replace_str/" /etc/nginx/sites-enabled/default


sudo service nginx restart
