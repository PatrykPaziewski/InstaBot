import time
import os
import sys
import subprocess
import signal

class CountdownTask: 
      
    def __init__(self):
        self._running = False 
      
    def terminate(self): 
        if self._running: 
            self.proc1.terminate()
            self._running = False
      
    def run(self): 
        if not self._running or self.check_if_terminated():
            self.start_subprocess()

    def start_subprocess(self):
        self.proc1 = subprocess.Popen('python application.py')
        self._running = True
        
    def check_if_terminated(self):
        if not self.proc1.poll() == None:
            return True