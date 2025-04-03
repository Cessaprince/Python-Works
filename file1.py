#INTERNSHIP ASSIGNMENT (QUESTION 2)

"""Geting three websites, 1 international and 2 local(Nigerian). 
Write a program that fetches the daily news headlines and links to the stories from these websites."""

#Importing the requests module and Beautiful soup module
import requests
from bs4 import BeautifulSoup

count = 0
while count < 3:
    print('')
    url = input('Enter URL: ')
    req = requests.get(url)
    html_page = req.content

    soup = BeautifulSoup(html_page, 'html.parser')
    title = soup.title.string
    print(f'For {title}:')
    print('')

    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        link = str(a_tag.get('href')).strip()
        text = str(a_tag.text).strip()

        if text == '' or link == '#':
            continue
        else:
            print(f'NEWS HEADLINE: {text}, LINK: {link}')

    count += 1

print('')


#INTERNSHIP ASSIGNMENT (QUESTION 1)
    
"""Writing a program that downloads all the images in a a given website."""

#import requests, beautifulsoup and os module
import requests
from bs4 import BeautifulSoup
import os

os.mkdir('Image Folder')  #make a new directory

url = 'https://www.booking.com/'
req = requests.get(url)
page = req.content #get the html content of the page

soup = BeautifulSoup(page, 'html.parser')

images = soup.find_all('img')  #find all the image tags

image_url_lst = []
for image in images:
    image_url = image.get('src')  #getting the url to the images
    image_url_lst.append(image_url)

print(f'The length of image_url_lst is {len(image_url_lst)}. Therefore last index is {len(image_url_lst) - 1}.')

count = 0
while count == 0:
    file_name = input('Enter the file name: ')
    index = int(input(f'Enter a number serving as index in list from 0 to {len(image_url_lst) - 1}: '))
    if file_name == '' or len(file_name) == 0 or index > len(image_url_lst) - 1:
        break
    else:
        url = image_url_lst[index]
        req = (requests.get(url)).content   #getting the binary content of the image
        file = open(f'Image Folder/{file_name}', 'wb+')
        file.write(req) #writing the content to a certain file in the ImageFolder directory
        

         
  


    

    
