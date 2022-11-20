import requests
from urllib.parse import urlparse
import os 
 
urls = [
     'https://election.thestar.com.my/json/PFT.json'
    ,'https://election.thestar.com.my/json/NJohor.json'
    ,'https://election.thestar.com.my/json/PJohor.json'
    ,'https://election.thestar.com.my/json/NKedah.json'
    ,'https://election.thestar.com.my/json/PKedah.json'
    ,'https://election.thestar.com.my/json/NKelantan.json'
    ,'https://election.thestar.com.my/json/PKelantan.json'
    ,'https://election.thestar.com.my/json/NMalacca.json'
    ,'https://election.thestar.com.my/json/PMalacca.json'
    ,'https://election.thestar.com.my/json/NNegeriSembilan.json'
    ,'https://election.thestar.com.my/json/PNegeriSembilan.json'
    ,'https://election.thestar.com.my/json/NPahang.json'
    ,'https://election.thestar.com.my/json/PPahang.json'
    ,'https://election.thestar.com.my/json/NPenang.json'
    ,'https://election.thestar.com.my/json/PPenang.json'
    ,'https://election.thestar.com.my/json/NPerak.json'
    ,'https://election.thestar.com.my/json/PPerak.json'
    ,'https://election.thestar.com.my/json/NPerlis.json'
    ,'https://election.thestar.com.my/json/PPerlis.json'
    ,'https://election.thestar.com.my/json/NSabah.json'
    ,'https://election.thestar.com.my/json/PSabah.json'
    ,'https://election.thestar.com.my/json/PSarawak.json'
    ,'https://election.thestar.com.my/json/NSarawak.json'
    ,'https://election.thestar.com.my/json/PSelangor.json'
    ,'https://election.thestar.com.my/json/NSelangor.json'
    ,'https://election.thestar.com.my/json/NOverview.json'
    ,'https://election.thestar.com.my/json/POverview.json'
    ,'https://election.thestar.com.my/json/01.json'
    ,'https://election.thestar.com.my/json/02.json'
    ,'https://election.thestar.com.my/json/03.json'
    ,'https://election.thestar.com.my/json/04.json'
    ,'https://election.thestar.com.my/json/05.json'
    ,'https://election.thestar.com.my/json/06.json'
    ,'https://election.thestar.com.my/json/07.json'
    ,'https://election.thestar.com.my/json/08.json'
    ,'https://election.thestar.com.my/json/09.json'
    ,'https://election.thestar.com.my/json/11.json'
    ,'https://election.thestar.com.my/json/12.json'
    ,'https://election.thestar.com.my/json/13.json'

]

def get_content(url):
    r = requests.get(url)
    return r.text

def write_file(filename,content):
    with open(f'E:\Desktop\github\Malaysia_General_election\GE15\{filename}',"w", encoding="utf-8") as f:
        f.write(content)

for url in urls:
    filename = os.path.basename(urlparse(url).path)
    raw = get_content(url)
    write_file(filename,raw)


