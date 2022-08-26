class Response:
    INIT = 'ini'
    UPDATE = 'upd'
    ERROR = 'err'

    def __init__(self, type, data):
        self.type = type
        self.data = data

