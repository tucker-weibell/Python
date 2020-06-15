import pyperclip
import threading 
 
def gfg(): 
    timer = threading.Timer(2.0, gfg) 
    timer.start()
    pyperclip.copy("I am watching you...") 

gfg()
