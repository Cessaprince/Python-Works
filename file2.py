"""HTTP Request in Python (Creating Sockets)."""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

print(ord('A'))



"""Using Beautiful Soup for Web Scraping."""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0 
atag_list = []
url = input('Enter url: ')
while count < 7:
    if count == 7:
        break
    else:
        html = urlopen(url, context = ctx).read()
        soup = BeautifulSoup(html, "html.parser")   
        # Retrieve all of the anchor tags
        a_tags = soup('a')   #list
        url = a_tags[17].get('href')
        atag_list.append(a_tags[17])
        count += 1

name_list = []
for a_tag in atag_list:
    name_list.append(a_tag.text)

print(name_list[len(name_list) - 1])



    

