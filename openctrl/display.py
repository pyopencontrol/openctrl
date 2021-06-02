import threading
try:
    from .grab import Image
except:pass
def grab_bytes():
    return Image().asbytes
def send(s,a):
    s.post(b's'+grab_bytes(),a)
def show_bytes(r):
    if not r.startswith('s'):return
    Image(r[1:]).show()
def conf(s,a):
    def _conf():
        while True:
            send(s,a)
    threading.Thread(target=_conf).start()
