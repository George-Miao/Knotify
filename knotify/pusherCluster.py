from .basePusher import BasePusher
from typing import List, Callable
from aiohttp import ClientSession


class PusherCluster:
    def __init__(self):
        self._pusher_list: List[BasePusher] = []
        self.session = ClientSession()
        pass

    def push(self, message="Empty Title", *args, **kwargs):
        for pusher in self._pusher_list:
            pusher.push(message=message)

    def register(self, pusher: Callable, **kwargs):
        self._pusher_list.append(pusher(session=self.session, **kwargs))

    def remove(self, pusher: BasePusher):
        self._pusher_list.remove(pusher)

    def __str__(self):
        return "\n".join(self._pusher_list)

    def __len__(self):
        return len(self._pusher_list)

    def __iter__(self):
        return self._pusher_list

    def __getitem__(self, item):
        return self._pusher_list[item]