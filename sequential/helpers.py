import time

def getResponseTimeInMillis(func, iterator):
  initialTime = time.time()
  for it in range(iterator):
    func()
  finalTime = time.time()

  return (finalTime - initialTime) * 1000