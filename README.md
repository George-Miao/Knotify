# Knotify

Knotify is a simple  tool that helps you to push notifications and other messages to the dedicated clients
Include Telegram Bot, Webhook, WirePusher, Wechat Bot (Server Chan)

## Quick Start
Use pip to install Knotify first:
```shell
pip install Knotify
```
Then inside your program:
```python
from Knotify import WirePusher
w = WirePusher("Your_Token_From_WirePusher")
w.push("FooBar")
```

## Requirement
Python 3.6+