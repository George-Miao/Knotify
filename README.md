# Knotify

Knotify is a simple tool that helps you to push notifications and other messages to the dedicated clients
Include Telegram Bot, Webhook, WirePusher, Wechat Bot (Server Chan)

## Quick Start
Use pip to install Knotify first:
```shell
pip install knotify
```
Then inside your program:
```python
from knotify import WirePusher
async with WirePusher("Your_Token_From_WirePusher") as w:
    w.emit("FooBar")
```

## Requirement
Python 3.6+

## License
MIT License