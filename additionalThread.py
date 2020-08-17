import time
import os
import subprocess

class CountdownTask: 
      
    def __init__(self): 
        self._running = True
      
    def terminate(self): 
        self._running = False
        os.system("taskkill -IM notepad.exe")
      
    def run(self): 
        if self._running: 
            subprocess.Popen(['notepad.exe'])

  