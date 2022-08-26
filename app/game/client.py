from app.game.gamestate import GameState
from app.game.request import Request
from app.game.response import Response

class Client:
    def __init__(self, proxy):
        self.proxy = proxy
        proxy.connect()

    def update(self):
        responses = self.proxy.get_responses()
        self.render(responses)
        while not (text := input('>> ')): pass
        self.proxy.send_request(Request(text))

    def render(self, responses):
        for response in responses:
            print(response.data)

