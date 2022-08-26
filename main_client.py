from app.game.client import Client
from app.proxy.clientproxy import ClientProxy

proxy = ClientProxy({'host':'127.0.0.1', 'port':8888})
client = Client(proxy)

while True:
    client.update()

