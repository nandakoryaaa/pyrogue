from app.command.command import Command
from app.game.gamestate import GameState
from app.game.request import Request
from app.game.response import Response
from app.command.command import Command
from app.command.movecommand import MoveCommand
from app.command.badcommand import BadCommand

class Server:
    def __init__(self, proxy):
        self.proxy = proxy
        self.game_states = {}
        proxy.set_server(self)

    def init_game(self, clid):
        game_state = GameState()
        game_state.set_data('--------@--------')
        self.game_states[clid] = game_state

        return game_state

    def update(self):
        requests = self.proxy.get_requests()
        out_responses = {}
        for clid in requests:
            command = self.create_command(requests[clid], self.game_states[clid])
            responses = command.execute()
            responses += self.process(self.game_states[clid])
            out_responses[clid] = responses

        self.proxy.send_responses(out_responses)

    def create_command(self, request, game_state):
        if request.type == Request.MOVE_L:
            return MoveCommand(game_state, 'L')
        elif request.type == Request.MOVE_R:
            return MoveCommand(game_state, 'R')

        return BadCommand()

    def process(self, game_state):
        return [Response(Response.UPDATE, game_state.map)]

