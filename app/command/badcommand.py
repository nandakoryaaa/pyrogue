from app.command.command import Command
from app.game.response import Response

class BadCommand(Command):
    def execute(self):
        return [Response(Response.ERROR, 'bad_command')]