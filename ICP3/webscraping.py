import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Deep_learning"
response = requests.get(url)

# Gets the html content
soup = BeautifulSoup(response.content, "html.parser")

# Finds the title of webpage
print("Title of the webpage is: ", soup.find(id='firstHeading').string)

# Writes all the links to outputfile
outFile = open('outputfile.txt' , 'w')
for r in soup.find_all('a'):
    outFile.write(str(r.get('href')) + '\n')
