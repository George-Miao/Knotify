from abc import ABC, abstractmethod

from requests import Session

from .utils import build_uri


class BasePusher(ABC):
    _scheme = "Knotify"

    def __init__(self, session: Session = None):
        self.loc = self.__class__.__name__
        if session:
            self.session = session
        else:
            self.session = Session()

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
        return "{}({})".format(self.__class__.__name__, self.uri)

