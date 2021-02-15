from django.shortcuts import render

from bs4 import BeautifulSoup
import requests
############################################################
source = requests.get("https://bdgovtjob.net/").text
soup = BeautifulSoup(source, 'lxml')

jobs_list = {}
for article in soup.find_all('article'):
    headline = article.h2.a.text
    link = article.find('h2', class_='entry-title').a['href']

    # print(headline)
    # print(link)
    # print()
    jobs_list[headline] = link

############################################################
source = requests.get("https://teletalkbd.com/")
soup = BeautifulSoup(source.text, 'lxml')

headlines= {}
for head in soup.find_all('li', class_='item clearfix'):
    h = head.a.text
    l = head.a['href']
    headlines[h] = l



# Create your views here.
def home(request):


    return render(request, 'home.html', {'bdgovtjobs': jobs_list, 'telejobs': headlines})