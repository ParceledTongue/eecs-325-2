# EECS 325
# Project 2 [bonus]
# Zachary Palumbo

import geoip2.database
import socket
from geopy.distance import vincenty
from urllib2 import urlopen

# Setup
reader = geoip2.database.Reader("GeoLite2-City.mmdb")  # load database
my_ip = urlopen('http://ip.42.pl/raw').read()  # IP address of the machine running the script
my_info = reader.city(my_ip)
my_location = (my_info.location.latitude, my_info.location.longitude)  # get our own latitude and longitude

# Get list of target sites
with open("targets.txt") as f:
    sites = f.read().splitlines()

# Main iteration
for site in sites:
    site_ip = socket.gethostbyname(site)
    site_info = reader.city(site_ip)
    site_location = (site_info.location.latitude, site_info.location.longitude)
    print("Distance to " + site + ": " + str(vincenty(my_location, site_location).miles) + " miles")
