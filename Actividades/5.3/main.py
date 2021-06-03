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

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                if item is _sentinel:
                    q.put(_sentinel)
                    break
                else:
                    logging.debug('Getting ' + str(item).split('/')[-1] + ' : ' + str(q.qsize()) + ' items in queue')
                    # Procesar el archivo
                    x = item.split("/")
                    x[-1] = x[-1].split(".")[0] + ".html"
                    salida = '/'.join(x)
                    resaltadorLexico(archivo=item, salida=salida)
        return


BUF_SIZE = 10
N = 10
PATH = "/Users/Pablo/Library/Mobile Documents/com~apple~CloudDocs/ITC/Semestre_4/MetodosComputacionales/repo/Actividades/5.3/test"
q = queue.Queue(BUF_SIZE)
    

if __name__ == '__main__':
    start_time = time.time()
    p = ProducerThread(name='producer', path=PATH)
    p.start()
    c = []
    for i in range(N):
        c.append(ConsumerThread(name=str(i)))
        c[i].start()
        
    while True:
        if p.done:
            p.join()
            for consumer in c:
                consumer.join()
            break
    
    print(f"No. hilos: {N} - Tiempo: {round(time.time() - start_time, 5)} seg.")
