from PIL import ImageGrab,Image
from .pilfullscreen import showPIL
import _io
def convert(i):
    if isinstance(i,bytes):
        return Image.frombytes(i)
    return i
def i2b(i,f="JPEG"):
    if isinstance(i,bytes):
        return i
    out=_io.BytesIO()
    i.save(out,format=f)
    return out.getvalue()
class Image:
    def __init__(self,img=ImageGrab.grab()):
        self.img=convert(img)  
        self.asbytes=i2b(img)
        self.window=None
    def destroy(self):
        if self.window:
            self.window.destroy()

    def show(self):
        self.destroy()
        self.window=showPIL(self.img)
    def send(self,sock,addr):
        sock.sendto(self.asbytes,addr)
    def __del__(self):
        self.destroy()
        
