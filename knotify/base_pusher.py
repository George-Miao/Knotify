from abc import ABC, abstractmethod
from typing import List, Dict, Tuple
from sys import stdout

import requests

from knotify.utils import build_uri
from knotify.exception import KnotifyException


class BasePusher(ABC):
    """
    Base classes for pushers
    Inherit from it and overload `_push` function to create custom pushers

    """
    _scheme = "Knotify"

    def __init__(self, show_message=True):
        """
        :param show_message: if set to True, the pusher will print out status and error message
        """
        self.name = self.__class__.__name__
        self.s = requests.Session()
        self.show_message = show_message

    def _push(self, message, **kwargs) -> bool:
        """
        Overload the this function to create custom pusher
        :param message: message to be sent
        :param kwargs: all params to be sent
            use function `_build_body` to build a dict for params
        :return: Returns true if pushing is succeeded, Otherwise False
        """
        pass

    @property
    @abstractmethod
    def uri(self) -> str:
        """
        :return: URI that can be used to pass information and create pusher instance with function `get_pusher`
        """
        pass

    def emit(self, message, **kwargs):
        """
        The actual emit function that's going to be used by users
        :param message: message to be sent
        :param show_message: 
        :return:
        """
        show_message = kwargs.pop("show_message", self.show_message)
        if show_message:
            stdout.write(f"Sending message to {self.name}... ")
        try:
            self._push(message, **kwargs)
            if show_message:
                print("Succeed")
        except Exception as e:
            if show_message:
                print("Failed, due to {}".format(e))

    def _format_uri(self, **kwargs):
        return build_uri(self._scheme, self.name, [], **kwargs)

    @staticmethod
    def _build_body(args, _dict, mandatory: List[str] = None, **defaults) -> Tuple[Dict[str, str], List]:
        """
        Build req_body(json or params) for request
        :param args: api params, will find each of args. Those who are not in defaults and are not mandatory will be
                        ignored
        :param _dict: a dict that contains everything (mostly the **kwargs from the invoke function)
        :param mandatory: mandatory items for api, if found missing items that's in the mandatory list,
                          will raise KnotifyException
        :param defaults: default KVs, will be replaced if exists in _dict
        :return: (body, ignored):
            body: The body built
            ignored: a list of ignored args
        """
        body = defaults
        ignored = []
        for arg in args:
            if arg in _dict:
                body[arg] = _dict.pop(arg)
            elif arg in mandatory and arg not in body:
                raise KnotifyException(f"Cannot find mandatory item {arg}")
            else:
                ignored.append(arg)

        return body, ignored

    @staticmethod
    def _check_result(result: requests.Response):
        if not result.ok:
            raise KnotifyException(result.reason)
        return result.ok

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, self.uri)
