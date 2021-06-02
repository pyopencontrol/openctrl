#!/usr/bin/env python3
import openctrl.sock as socket_
import pickle
s=socket_.Socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('gtsforum.xyz',6352))
def main():
        reg=None
        wut={}
        while True:
            data,addr=s.receive()
            """
            if data==b"\x04\x01":
                if addr in reg:
                        s.sendto(b'\x01\x00',addr)
                        continue
                reg.append(addr)
                s.sendto(b'\x00',addr)
            elif data==b"\x05\x00":
                s.sendto(pickle.dumps(reg),addr)
            elif data.startswith(b"\x00\x11\x22"):
                dt=data[:2]
                try:
                    d=pickle.loads(dt)
                except:
                    s.sendto(b'\x01\x00',addr)
                    continue
                if d not in reg:
                    wut[addr]=d
                    wut[d]==addr
                    s.sendto(b'\x02',addr)"""
            if data==b'r':
                if reg:
                    wut[reg]=addr
                    wut[addr]=reg
                    s.post(b'\x00',addr)
                    s.post(b'\x00',reg)
                    reg=None
                else:

                    reg=addr
                    s.post(b'\x02',addr)
            else:
                if addr in wut:
                    s.post(data,wut[addr])
                else:

                    s.post(b'\x01',addr)
            print(reg)
            print(wut)

                    

main()  
