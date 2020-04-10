from knotify import WirePusher

a = WirePusher("aaa")
m = a.verify_msg(123)
print(m)
print(a)

