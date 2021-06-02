from . import sock as socket
from .clients import *
import builtins
sock=socket.Socket(socket.AF_INET,socket.SOCK_DGRAM)
builtins.servadd=('gtsforum.xyz',6352)
def main(wtd=False):
    while True:
      f=sock.receive()[0]
      if f==b'\x00':
        break
    if wtd:
        controlled(sock)
    else:
        controller(sock)
        
    
  
def connect():
    sock.sendto(b'r',servadd)
    print(f'Your Adress is  {sock.getsockname()}')
    f=sock.receive()[0]
    if f==b'\x02':
        print(f'Please wait as somebody join...')
        main(True)
    main()
