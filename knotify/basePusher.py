from abc import ABC, abstractmethod
from typing import Union
from asyncio import run

from aiohttp import ClientSession

from .message import Msg
from .utils import build_uri


class BasePusher(ABC):
    _scheme = "Knotify"

    def __init__(self, session: ClientSession = None):
        self.loc = "BasePusher"
        if session:
            self.session = session
        else:
            self.session = ClientSession()

    @staticmethod
    def verify_msg(message) -> Union[str, Msg]:
        if isinstance(message, str):
            message = Msg(None, message)
        elif not isinstance(message, Msg):
            raise TypeError(f"Expect {Msg} or {str}, get {message.__class__} instead")
        return message

    @abstractmethod
    def push(self, message, **kwargs):
        pass

    @property
    @abstractmethod
    def uri(self):
        pass

    def _format_uri(self, **kwargs):
        return build_uri(self._scheme, self.loc, [], **kwargs)

    def __str__(self):
        return "{}(uri={})".format(self.__class__.__name__, self.uri)

    def __del__(self):
        run(self.session.close())
