from app.game.server import Server
from app.game.client import Client
from app.proxy.proxy import Proxy
from app.game.server import Server

proxy = Proxy()
server = Server(proxy)
client = Client(proxy)

while True:
    client.update()
    server.update()


