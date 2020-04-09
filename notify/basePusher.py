from abc import ABC, abstractmethod


class BasePusher(ABC):
    def __init__(self, token):
        self.token = token

    @abstractmethod
    def push(self, message, title=""):
        pass

    def __str__(self):
        return "[Pusher {}, Token: {}]".format(self.__class__, self.token)


def get_pusher(token: str):
