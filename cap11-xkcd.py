import requests, os, bs4
#My internet connection is slow, so i changed the code to get the title instead of the image
url = 'http://xkcd.com'
number = ''
while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    selectedText = soup.select('#ctitle')[0].get_text()
    if selectedText == []:
        print('No title found.')
    else:
        print(number + ': ' + selectedText)
    url = 'http://xkcd.com' + soup.select("a[rel='prev']")[0].get('href')
    number = soup.select("a[rel='prev']")[0].get('href').replace('/','')
