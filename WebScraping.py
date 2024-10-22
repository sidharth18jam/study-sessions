#! python3
# WebScraping.py - opens several google search results.

import requests, sys, webbrowser, bs4

print ('Googling .....')

res = requests.get('https://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))