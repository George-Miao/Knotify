from knotify import Telegram, WirePusher, Webhook, Wechat
import asyncio

a = "SCU93196T8befabe03394ad3de83e17f24f686ec05e8ec91a1a145"


async def main():
    w = Wechat(a)
    await w.emit("Fine")
    await w.close()


loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())
loop.close()


