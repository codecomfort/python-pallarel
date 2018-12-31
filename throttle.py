from threading import Lock


class Throttle:
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0.0
        self.last = 0

    def consume(self, amount=1):
        pass
