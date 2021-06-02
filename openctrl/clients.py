from .mouse import *
from .display import *
def controller(sock):
    config(sock,servadd)
    while True:
        ss=sock.receive()[0]
        show_bytes(ss)
def controlled(sock):
    conf(sock,servadd)
    while True:
        ss=sock.receive()[0]
        parse(ss)
                
        
         

