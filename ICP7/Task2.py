# 2&3 Extract the following web URL text using BeautifulSoup and Save it in input.txt
from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/Google'
response = requests.get(url)

# Gets the html content
soup = BeautifulSoup(response.text, "html.parser")

f1 = open("input.txt", "w")
output = ''
for i in soup.find_all('p'):
    output = str(output) + i.text
f1.write(str(output))
f1.close()
