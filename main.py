import time
import os

from additionalThread import CountdownTask

class main():
    def __init__(self, *args, **kwargs):
        self.started = False
        self.c = CountdownTask()
        self.main_loop()

    def start(self):
        if not self.started:
            self.c.run() 
            self.clear()
            self.started = True

    def stop(self):
        if self.started:
            self.c.terminate()
            self.clear()
            self.started = False
            
    def clear(self):
        os.system("cls")
                
    def main_loop(self):
        text = None
        while text != "exit":
            if  text == "start":
                self.start()
                
            if  text == "stop":
                self.stop()
            text = input()
                



if __name__ == "__main__":
    main()