# Knotify

Knotify is a simple tool that helps you to push notifications and other messages to the dedicated clients
Include Telegram Bot, Webhook, WirePusher, Wechat Bot (Server Chan)

## Quick Start
Use pip to install Knotify first:
```shell
pip install knotify
```

Then get the "key" from the client you want to use:
- [Webhook](#Webhook)
- [Wechat](#Wechat)
- [Telegram](#Telegram)
- [WirePusher](#WirePusher)

Use context manager for a quick and easy notification:
```python
from knotify import WirePusher
async def main():
    async with WirePusher("Your_Token_From_WirePusher") as w:
        w.emit("FooBar")
```

If you want to keep the instance for a longer lifespan, remember to use ``await PusherInstance.close()`` afterwards:
```python
from knotify import WirePusher
async def main():
    w = WirePusher("Your_Token_From_WirePusher")            
    await w.emit("Foo")
    await w.emit("Bar")
    await w.close()
```
## Pre-defined Pushers
### Webhook
The "key" will be the url you want to post to itself

e.g. [Discord Server Webhook](https://support.discordapp.com/hc/en-us/articles/228383668)

### Wechat
The wechat client is [Server Chan(Server酱)](http://sc.ftqq.com/3.version) and the key will be `sckey`

### Telegram
The telegram client is `tg_push_bot` from Fndroid. [Use Manual](https://github.com/Fndroid/tg_push_bot/blob/master/README.md)

### WirePusher
[WirePusher](http://wirepusher.com/) is an Android app that allows you to send push notifications right to your device.

## Custom Pusher
Create a custom pusher by inheriting from `BasePusher`:
```python
class CustomPusher(BasePusher):
    pass
```
And all you need to do is to overload the `_push` function which will be invoked by `emit` function:
```python
async def _push(self, message, **kwargs) -> bool:
    """
    Overload this function to create custom pusher
    :param message: message to be sent
    :param kwargs: all params to be sent
        use function `_build_body` to build a dict for params
    :return: Returns True if pushing is succeeded, Otherwise False
    """
    pass
```
Use the built-in `aiohttp.ClientSession` to invoke http api and `self._check_result` to check result:
```python
async def _push(self, message, **kwargs) -> bool:
    with self.s.get("api", data=kwargs) as result:
        return self._check_result(result)
```


## Requirement
- Python 3.6+
- aiohttp
- 

## License
MIT License
