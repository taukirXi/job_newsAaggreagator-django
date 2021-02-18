from bs4 import BeautifulSoup
import requests

def bdgovtjob():
    bdjobs = requests.get("https://bdgovtjob.net/").text
    soup = BeautifulSoup(bdjobs, 'lxml')

    jobs_list = {}
    for article in soup.find_all('article'):
        headline = article.h2.a.text
        link = article.find('h2', class_='entry-title').a['href']

        # print(headline)
        # print(link)
        # print()
        jobs_list[headline] = link


    return jobs_list


def telebd():
    tele = requests.get("https://teletalkbd.com/")
    soup = BeautifulSoup(tele.text, 'lxml')

    headlines = {}
    for head in soup.find_all('li', class_='item clearfix'):
        h = head.a.text
        l = head.a['href']
        headlines[h] = l

    return headlines


