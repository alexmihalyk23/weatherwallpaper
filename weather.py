#!/usr/bin/env python3
import requests
import time
import os
import socket
REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

while True:
    if is_connected(REMOTE_SERVER):
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city = 'Akademgorodok'
        url = api_address + city
    
        json_data = requests.get(url).json()
        format_add = json_data['weather'][0]['main']
        if format_add == 'Snow':
            os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/$USER/Snow.jpg")
            time.sleep(5)
        elif format_add == 'Clear':
            os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/$USER/Clear.jpg")
            time.sleep(5) #1800
        elif format_add == 'Clouds':
            os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/$USER/Clouds.jpg")
            time.sleep(5)
        else:
            os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/$USER/dark.png")
            time.sleep(5)
    else:
        os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/$USER/dark.png")
