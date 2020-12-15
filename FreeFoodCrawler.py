import requests
from bs4 import BeautifulSoup
import webbrowser

url_head = "https://moltke.nccu.edu.tw/Registration/"
matches = ['食物','餐盒','午餐','晚餐','供餐','點心']

def getSoup(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'html.parser')
    return soup

def checkFood(url):
    soup = getSoup( url )
    # print(soup.prettify())
    for paragraph in soup.findAll('p'):
        content = paragraph.text.strip()
        if any(x in content for x in matches):
            print(soup.title.string)
            print(url)
            return url
    return None

# new event webpage
soup = getSoup(url_head+"registration.do?action=new")

# Get all events
conference_list = []
for h4 in soup.findAll('h4'):
    for a in h4.findAll('a'):
        conference_list.append(url_head + str(a['href']))

for i in conference_list:
    if(checkFood(i)):
        webbrowser.get().open_new_tab(i)


