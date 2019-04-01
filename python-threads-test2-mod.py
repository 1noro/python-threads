#!/usr/bin/env python

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print( self.getName()+": started!" )
        for i in range(1, 11):
            # time.sleep(1)
            print(self.getName()+": "+str(i))
        print( self.getName()+": finished!" )

def main():
    for x in range(4):
        mythread = MyThread( name = "T"+str(x + 1) )
        mythread.start()
        # time.sleep(.9)

if __name__ == '__main__': main()
