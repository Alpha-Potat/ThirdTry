import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN=getenv("TOKEN_BOT")
url="nikita-slomal.ru:8443"
path='./cert/YOURPUBLIC.pem'


def setWebhook(url: str = url, path: str = path):
    whook = url
    inputfile = path
    files = {"certificate": open(inputfile, "r")}
    if path == None:
        r = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://{whook}')
        print(r.json())
    elif path != None:
        r = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://{whook}',
                               files=files)
        print(r.json())

