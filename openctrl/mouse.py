try:
    from pynput.mouse import *
except:
    import warnings
    warnings.warn(UserWarning("No X server running."))
import pickle
try:
    mouse=Controller()
except:pass
def parse(opt):
    if not opt.startswith(b'm'):
        return
    opt=opt[1:]
    if opt.startswith(b'm'):
        pick=pickle.loads(opt[2:])
        mouse.position=pick
    elif opt.startswith(b'c'):
        pick=pickle.loads(opt[2:])
        mouse.position=pick
        mouse.press(Button.left)
        mouse.release(Button.left)
        

def config(s,a):
    def move(x,y):
        data=b'mm'+pickle.dumps((x,y))  
        s.post(data,a)
    def click(x,y,b,r):
        data=b'mc'+pickle.dumps((x,y))  
        s.post(data,a)
    listen=Listener(on_move=move,on_click=click)
    listen.start()


