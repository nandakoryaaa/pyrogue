import socket

from app.game.response import Response
from app.game.gamestate import GameState

class ClientProxy:
    def __init__(self, config):
        self.config = config
        self.socket = None
        self.game_state = GameState()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.config['host'], self.config['port']))

    def send_request(self, request):
        bytes = self.encode_request(request)
        self.socket.send(bytes)

    def get_responses(self):
        text = self.socket.recv(2048).decode()
        if text:
            return self.decode_responses(text)
        return None

    def encode_request(self, request):
        text = request.type
        if request.params is not None:
            text += ' '.join(request.params)
        return text.encode()

    def decode_responses(self, text):
        responses = []
        lines = text.split("\n")
        for line in lines:
            type, data = line.split(' ')
            self.update_state(type, data)
            responses.append(Response(type, data))
        return responses

    def update_state(self, type, data):
        if type == Response.INIT:
            self.game_state.set_data(data)
        else:
            self.game_state.set_data(data)