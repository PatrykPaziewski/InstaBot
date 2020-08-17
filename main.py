import time
from threading import Thread 

from additionalThread import CountdownTask

class main():
    def __init__(self, *args, **kwargs):
        self.c = CountdownTask() 
        self.t = Thread(target = self.c.run) 
        self.main_loop()

    def start(self):
        self.t.start() 

    def stop(self):
        self.c.terminate()
                
    def main_loop(self):
        text = input()
        while text != "stop":
            if  text == "start":
                self.start()
            text = input()
            
        if  text == "stop":
            self.stop()



if __name__ == "__main__":
    main()