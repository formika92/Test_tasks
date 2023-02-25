class NotAllowedMethod(Exception):
    def __init__(self, attrs) -> None:
        self.message = f"Attributes or methods {attrs} not allowed"

    def __str__(self):
        return self.message
