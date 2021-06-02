from socket import *
import _io
class Socket(socket):
    def __init__(self,*args,**kwargs):
        bufsize=kwargs.get("bufsize",1024)
        if bufsize<10:
            raise ValueError("buffer too small")
        self.bufsize=bufsize
        if "bufsize" in kwargs:
            del kwargs["bufsize"]
        super().__init__(*args,**kwargs)
    def receive(self):
        result=b""
        inmsg=False
        addr=None
        while True:
            m=self.recvfrom(self.bufsize)
            addr=m[1]
            m=m[0]
            if m==b'\x00':
                inmsg=True
            elif inmsg:
                result+=m
            elif m==b'\xff':
                inmsg=False
                break
        return result,addr
    def post(self,data,addr):
        
        data=_io.BytesIO(data)
        self.sendto(b'\x00',addr)
        while True:
            bs=data.read(self.bufsize)
            self.sendto(bs,addr)
        self.sendto(b'\xff',addr)
        return len(data.getvalue())

