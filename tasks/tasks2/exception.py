class InvalidFileName(Exception):
    def __init__(self, msg) -> None:
        self.message = msg

    def __str__(self):
        return self.message
