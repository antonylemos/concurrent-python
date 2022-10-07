import time
from threading import Thread

def getResponseTimeInMillis(func, iterator):
  initialTime = time.time()

  threads = []

  for it in range(iterator):
    thread = Thread(target=func)
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()
  
  finalTime = time.time()

  return (finalTime - initialTime) * 1000