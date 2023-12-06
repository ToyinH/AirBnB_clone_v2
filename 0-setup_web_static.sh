#!/usr/bin/env bash
# Preparing my webservers with this script
sudo apt-get update

sudo apt-get install -y nginx

sudo ufw allow 'Nginx HTTP'

sudo mkdir /data/

sudo mkdir /data/web_static/

sudo mkdir /data/web_static/releases/

sudo mkdir /data/web_static/shared/

sudo mkdir /data/web_static/releases/test/


# sudo mkdir -p /data/web_static/releases/test/

# sudo mkdir -p /data/web_static/shared/

cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

sym_link="/data/web_static/current"

target="/data/web_static/releases/test/"

if [ -L "$sym_link" ]; then
		sudo rm -rf "$sym_link"
fi

sudo ln -s "$target" "$sym_link"

sudo chown -R "$USER":"$USER" /data/

replace_str="server_name _;\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"

sudo sed -i "s|server_name _;|$replace_str|" /etc/nginx/sites-enabled/default


sudo service nginx restart
