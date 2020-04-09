from .basePusher import BasePusher


class PusherCluster:
    def __init__(self):
        self._pusher_list = []
        pass

    def push(self, title, message="", *args, **kwargs):
        pass

    def register(self, pusher: BasePusher):
        self._pusher_list.append(pusher)

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