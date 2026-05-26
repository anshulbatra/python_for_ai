import requests
from bs4 import BeautifulSoup
from lxml import html   

#Useful packages in python

#requests
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())

#beautifulsoup4
html_content = BeautifulSoup(response.content, 'html.parser')
print(html_content.prettify())

#lxml
doc = html.fromstring(response.content)
print(html.tostring(doc, pretty_print=True).decode('utf-8'))
#Extracting links
links = doc.xpath('//a/@href')
print(links)
links2 = doc.xpath('//a/text()')
print(links2)

