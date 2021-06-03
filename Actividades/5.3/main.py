import logging
import queue
import os
import threading
import time
from lexico import resaltadorLexico

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)
_sentinel = object()

class ProducerThread(threading.Thread):
    def _init_(self, path: str, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self)._init_()
        self.path = path
        self.target = target
        self.name = name
        self.done = False

    def run(self):
        gen = self.generator()
        while True:
            try:
                if not q.full():
                    item = next(gen)
                    q.put(item)
                    logging.debug('Putting ' + str(item).split('/')[-1]  + ' : ' + str(q.qsize()) + ' items in queue')
            except StopIteration:
                logging.debug("=== NO ITEMS LEFT TO INSERT ===")
                self.done = True
                q.put(_sentinel)
                break
        return
    
    def generator(self):
        path = self.path
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                continue
            yield os.path.join(path, file)