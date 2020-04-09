from .basePusher import BasePusher
from requests import request


class Webhook(BasePusher):
    def push(self, message, title=""):
        pass


class Telegram(BasePusher):
    def push(self, message, title=""):
        pass


class Wechat(BasePusher):
    def push(self, message, title=""):
        pass


class WirePusher(BasePusher):
    def push(self, message, title=""):
        pass


