from aiohttp import ClientSession

from .basePusher import BasePusher
from .message import Msg

__all__ = ["Webhook", "Telegram", "Wechat", "WirePusher"]


class Webhook(BasePusher):
    def __init__(self, key, session: ClientSession = None):
        super().__init__(session)
        self.key = key

    def push(self, message, **kwargs):
        message = self.verify_msg(message)

    @property
    def uri(self):
        return super()._format_uri(key=self.key)


class Telegram(BasePusher):
    def __init__(self, key, session: ClientSession = None):
        super().__init__(session=session)
        self.key = key
        self.api = ""

    def push(self, message, **kwargs):
        message = self.verify_msg(message)

    @property
    def uri(self):
        pass


class Wechat(BasePusher):
    def __init__(self, key, session: ClientSession = None):
        super().__init__(session=session)
        self.key = key

    def push(self, message, **kwargs):
        message = self.verify_msg(message)

    @property
    def uri(self):
        pass


class WirePusher(BasePusher):
    def __init__(self, key, session: ClientSession = None):
        super().__init__(session=session)
        self.key = key

    def push(self, message, **kwargs):
        message = self.verify_msg(message)

    @property
    def uri(self):
        pass


