from typing import List, Callable, Union
from sys import stdout

from knotify.base_pusher import BasePusher


class PusherCluster:
    def __init__(self, show_message=True):
        self._pusher_list: List[BasePusher] = []
        self.show_message = show_message

    def emit(self, message="Empty Message", **kwargs):
        show_message = kwargs.pop("show_message", self.show_message)
        for pusher in self._pusher_list:
            pusher.emit(message, show_message=show_message, **kwargs)
        return self

    def add(self, pusher: Union[BasePusher, List[BasePusher]]):
        if isinstance(pusher, list):
            self._pusher_list.extend(pusher)
        else:
            self._pusher_list.append(pusher)
        return self

    def remove(self, pusher: BasePusher):
        self._pusher_list.remove(pusher)
        return self

    def __str__(self):
        return "PusherCluster({})".format(", ".join([str(x) for x in self._pusher_list]))

    def __len__(self):
        return len(self._pusher_list)

    def __iter__(self):
        return self._pusher_list

    def __getitem__(self, item):
        return self._pusher_list[item]