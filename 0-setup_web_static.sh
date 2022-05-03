#!/usr/bin/env bash
#Install Nginx if it not already installed
#Create the folder /data/ if it doesn’t already exist
#Create the folder /data/web_static/ if it doesn’t already exist
#Create the folder /data/web_static/releases/ if it doesn’t already exist
#Create the folder /data/web_static/shared/ if it doesn’t already exist
#Create the folder /data/web_static/releases/test if it doesn’t already exist
#Create a fake HTML file /data/web_static/releases/test/index.html
#sym. link /data/web_static/current linked to /data/web_static/releases/test
#Give ownership of the /data/ folder to the ubuntu user AND group
#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static

apt-get update
apt-get install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t</body>\n</html>\n" > /data/web_static/current/index.html

ln -fs /data/web_static/current /data/web_static/releases/test/

chown -R ubuntu:ubuntu /data/

sed -i '/$/a location /hbnb_static {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-availables/default
service nginx restart
