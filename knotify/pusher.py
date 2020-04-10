from urllib import parse

from requests import Session

from .basePusher import BasePusher
from .exception import KnotifyException

__all__ = ["Webhook", "Telegram", "Wechat", "WirePusher", "get_pusher"]


class Webhook(BasePusher):
    def __init__(self, url, session: Session = None):
        super().__init__(session)
        self.url = url

    def push(self, message, **kwargs) -> int:
        result = self.session.post(self.url, json={"content": "[Knotify] " + message})
        if not result.ok:
            raise KnotifyException(f"Failed to post massage to webhook\n"
                                   f"Detail Info: {result.text}")
        return result.status_code

    @property
    def uri(self):
        return self._format_uri(url=self.url)


class Telegram(BasePusher):
    api = "https://tgbot.lbyczf.com/sendMessage/"

    def __init__(self, token, session: Session = None):
        super().__init__(session=session)
        self.token = token

    def push(self, message, **kwargs):
        req_body = {
            "text": message,
            "parse_mode": "Markdown"
        }
        result = self.session.post(self.api + self.token, json=req_body)
        if not result.ok:
            raise KnotifyException(f"Failed to post massage to Telegram\n"
                                   f"Detail Info: {result.text}")
        return result.status_code

    @property
    def uri(self):
        return self._format_uri(token=self.token)


class Wechat(BasePusher):
    def __init__(self, sckey, session: Session = None):
        super().__init__(session=session)
        self.key = sckey

    def push(self, message, **kwargs):
        pass

    @property
    def uri(self):
        return self._format_uri(sckey=self.sckey)


class WirePusher(BasePusher):
    def __init__(self, pid, session: Session = None):
        super().__init__(session=session)
        self.pid = pid

    def push(self, message, **kwargs):
        pass

    @property
    def uri(self):
        return self._format_uri(pid=self.pid)


def get_pusher(uri: str):
    result: parse.ParseResult = parse.urlparse(uri)
    if result.scheme != "knotify":
        raise KnotifyException("Invalid url scheme")
    params = dict(parse.parse_qsl(result.query))
    try:
        return eval(f"{result.netloc}(**params)")
    except Exception as e:
        raise KnotifyException(e)
