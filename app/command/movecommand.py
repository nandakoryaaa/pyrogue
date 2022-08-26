from app.command.command import Command


class MoveCommand(Command):
    def execute(self):
        data = self.game_state.map
        if self.params == 'L':
            data = data.replace('-@', '@-', 1)
        elif self.params == 'R':
            data = data.replace('@-', '-@', 1)

        self.game_state.map = data

        return []
