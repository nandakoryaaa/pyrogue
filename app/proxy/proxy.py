from app.game.response import Response

class Proxy:
    def __init__(self):
        self.server = None
        self.game_state = None
        self.requests = { 1: None }
        self.responses = []

    def connect(self):
        self.game_state = self.server.init_game(1)
        self.responses = [Response(Response.INIT, self.game_state.map)]

    def set_server(self, server):
        self.server = server

    def get_requests(self):
        return self.requests

    def send_request(self, request):
        self.requests[1] = request

    def get_responses(self):
        return self.responses

    def send_responses(self, responses):
        self.responses = responses[1]

