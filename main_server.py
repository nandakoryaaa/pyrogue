from app.game.server import Server
from app.proxy.serverproxy import ServerProxy

proxy = ServerProxy({'host':'127.0.0.1', 'port':8888})
server = Server(proxy)
proxy.set_server(server)
proxy.init()

while True:
    server.update()

