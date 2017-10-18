#! /usr/bin/python3
import requests, sys, webbrowser, bs4

if len(sys.argv) <= 1:
    print('Please insert a search query! ')
else:
    res = requests.get('http://www.google.com.br/search?q='+' '.join(sys.argv[1:]))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    selectSoup = soup.select('.r a')
    minOpen = min(5, len(selectSoup)) #Mininum of possible results
    for i in range(minOpen):
        webbrowser.open('http://www.google.com.br/' + selectSoup[i].get('href'))
