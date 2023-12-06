#!/usr/bin/env bash
# Preparing my webservers with this script


sudo mkdir -p /data/web_static/releases/test/

sudo mkdir -p /data/web_static/shared/

echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

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
