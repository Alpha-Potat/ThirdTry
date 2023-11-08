import ssl

from fastapi import FastAPI
import uvicorn
from os import getenv
from dotenv import load_dotenv

from swh import setWebhook
from models import User
from sendMessage import sendMessage

load_dotenv()
TOKEN=getenv("TOKEN_BOT")
WEBHOOK_SSL_CERT="./cert/YOURPUBLIC.pem"
WEBHOOK_SSL_PRIV="./cert/YOURPRIVATE.key"

app = FastAPI()

@app.post("/")
async def echo(obj:User):

    if obj.message.text=="/start":
        data = {
            'chat_id': obj.message.from_f.id,
            'text': f"Приветствую, {obj.message.from_f.username}"
        }
        await sendMessage(TOKEN, data)

    else:
        data={
            'chat_id' : obj.message.from_f.id,
            'text' : obj.message.text
        }
        await sendMessage(TOKEN, data)
    return {"ok":"ok"}

if __name__=="__main__":
    setWebhook()
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)
    uvicorn.run(app=app, host="0.0.0.0", port=8447, ssl_keyfile=WEBHOOK_SSL_PRIV, ssl_certfile=WEBHOOK_SSL_CERT)


