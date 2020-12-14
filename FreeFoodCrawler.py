import requests
from bs4 import BeautifulSoup
import webbrowser

url_head = "https://moltke.nccu.edu.tw/Registration/"
matches = ['食物','餐盒','午餐','晚餐','供餐','點心']

def getSoup(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'html.parser')
    return soup

def checkFood(short_url):
    soup = getSoup( url_head + str(short_url))
    # print(soup.prettify())
    for paragraph in soup.findAll('p'):
        content = paragraph.text.strip()
        if any(x in content for x in matches):
            return url_head+str(short_url)
    return None

# new event webpage
soup = getSoup("https://moltke.nccu.edu.tw/Registration/registration.do?action=new")

# Get all events
conference_list = []
for h4 in soup.findAll('h4'):
    for a in h4.findAll('a'):
        conference_list.append(a['href'])

for i in conference_list:
    if(checkFood(i)):
        webbrowser.get().open_new_tab(checkFood(i))


