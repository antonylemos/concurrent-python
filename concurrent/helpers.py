import time
from threading import Thread

def getResponseTimeInMillis(func, iterator):
  initialTime = time.time()

  threads = []
  for i in range(1, 9):
    t = Thread(target=theadManager, args=(func, iterator, ))
    threads.append(t)
    t.start()

  for t in threads:
    t.join()

  finalTime = time.time()

  return (finalTime - initialTime) * 1000


def theadManager(func, iterator):
  print(iterator)
  while(iterator <= 0):
    iterator -= 1
    print(iterator)
    func()