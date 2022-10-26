from http.client import HTTPResponse
from logging import _srcfile
from django.shortcuts import render
from django.http import HttpResponse
import requests

from bs4 import BeautifulSoup
import csv
from django import forms
import urllib

def home(request):
    return render(request, 'home.html',{'name': 'Jesus Menera'})

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
}

def add(request):
    number1 = request.POST['number1']
    res = number1
    x = request.POST['number1']

    source = requests.get(x).text
    source = se.get(x).text
    soup = BeautifulSoup(source, 'html.parser')
    try:
        title = soup.title.text
        print("Title: " + title)
    except Exception as e:
        title = None
        print('Title: ', title)
    try:
        title_length = soup.title.text
        print('Title Lenght:', len(title_length))
    except Exception as e:
        title_length = None
        print('Title Lenght:', title_length)
    try:
        description = soup.find("meta", attrs={'name':'description'})
        print('Description:', (description['content']))
    except Exception as e:
        print(e)
        #return  None
        #print('Description:', (description['content']))
    try:
        description_length = soup.find('meta', attrs={'name':'description'})
        print('Description Length:', len(description_length['content']))
    except Exception as e:
        description_length = None
        print('Description Length:', description_length)
    try:
        h1 = soup.find('h1').text
        print('Heading H1:', h1)
    except Exception as e:
        h1 = None
        print('Heading H1:', h1)
    try:
        h2 = soup.find('h2').text
        print('Heading H2:', h2)
    except Exception as e:
        h2 = None
        print('Heading H1:', h2)
    try:
        h3 = soup.find('h3').text
        print('Heading H3:', h3)
    except Exception as e:
        h3 = None
        print('Heading H3:', h3)
    try:
        h4 = soup.find('h4').text
        print('Heading H4:', h4)
    except Exception as e:
        h4 = None
        print('Heading H4:', h4)
    try:
        h5 = soup.find('h5').text
        print('Heading H5:', h5)
    except Exception as e:
        h5 = None
        print('Heading H5:', h5)
    try:
        h6 = soup.find('h6').text
        print('Heading H6:', h6)
    except Exception as e:
        h6 = None
        print('Heading H6:', h6)        
    try:
        EmptyImage_altribute = soup.find_all('img', alt='')
        print('Alt Empty Number of Images:', len(EmptyImage_altribute))
    except Exception as e:
        print('Alt Empty Number of Images:', len(EmptyImage_altribute)) 
        

    return render(request, 'result.html',{'Result':res, 'title':title,
                                        'title_length':len(title_length),
                                        'description':description['content'],
                                        'description_length':len(description_length['content']),
                                        'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6,
                                        'image':len(EmptyImage_altribute),
                                        'EmptyImage_altribute':EmptyImage_altribute,
                                        })