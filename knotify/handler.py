import logging
from typing import List

from .base_pusher import BasePusher
from .exception import KnotifyException


class KnotifyHandler(logging.Handler):
    def __init__(self, pushers, level=logging.NOTSET, formatter=None):
        super().__init__(level)
        self.pushers: List[BasePusher]
        if isinstance(pushers, BasePusher):
            self.pushers = [pushers]
        elif isinstance(pushers, list):
            self.pushers = pushers
        else:
            raise TypeError(f"Expect BasePusher or List[BasePusher] for `pushers`, get {pushers.__class__.__name__} instead")
        self.formatter = formatter or logging.Formatter("%(asctime)s [Knotify]: %(message)s")

    def emit(self, record):
        msg = self.formatter.format(record)
        for pusher in self.pushers:
            try:
                pusher._push(msg)
            except KnotifyException as e:
                print(f"Unable to push message to {pusher.uri} due to {e}")

