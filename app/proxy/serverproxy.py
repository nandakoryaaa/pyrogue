import socket
import select
import time

from app.game.response import Response
from app.game.request import Request

class ServerProxy:
    def __init__(self, config):
        self.srv_socket = None
        self.config = config
        self.server = None
        self.game_states = {}
        self.sockets = {}

    def init(self):
        self.srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srv_socket.bind((self.config['host'], self.config['port']))
        self.srv_socket.setblocking(False)
        self.srv_socket.listen()

    def set_server(self, server):
        self.server = server

    def get_requests(self):
        requests = {}
        while True:
            self.accept_connections()
            if len(self.sockets):
                read, write, ex = select.select(self.sockets, [], [], 0)
                for clid in read:
                    sock = self.sockets[clid]
                    text = sock.recv(2048).decode()
                    if len(text) == 0:
                        self.disconnect(clid, sock)
                        continue
                    print("<< " + text)
                    requests[clid] = self.decode_request(text)
                if len(requests) > 0:
                    break
            time.sleep(0.1)
        return requests

    def send_responses(self, responses):
        for clid in responses:
            sock = self.sockets[clid]
            out = []
            for response in responses[clid]:
                out.append(self.encode_response(response))
            sock.send("\n".join(out).encode())
            print(">> " + str(out))

    def decode_request(self, text):
        chunks = text.split(' ')
        data = chunks[1] if len(chunks) > 1 else None
        request = Request(chunks[0], data)

        return request

    def encode_response(self, response):
        return (response.type + ' ' + response.data)

    def accept_connections(self):
        read, write, ex = select.select([self.srv_socket], [], [], 0)
        if len(read):
            sock, addr = self.srv_socket.accept()
            sock.setblocking(False)
            clid = sock.fileno()
            print("*** connect: " + str(clid))
            self.sockets[clid] = sock
            self.game_states[clid] = self.server.init_game(clid)
            response = Response(Response.INIT, self.game_states[clid].map)
            l = sock.send(self.encode_response(response).encode())

    def disconnect(self, clid, sock):
        sock.close()
        del self.sockets[clid]
        print("*** disconnect: " + str(clid))

