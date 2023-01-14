import socket
from ip2geotools.databases.noncommercial import DblpCity

url = input("Insere a URL: ")
IP = socket.gethostbyname(url)
response = DblpCity.get(IP, api_key='free')

print("IP:", IP)
print('City:', response.city)
print("Region:", response.region)
print("Country", response.country)

