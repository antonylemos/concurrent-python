from helpers import getResponseTimeInMillis
from request_controller import getCoffeeImageUrl

def runSceneries(scenerie, amountOfExecutions):
  file_name = "concurrent/data/scenerie_%d.csv"%(scenerie)
  f = open(file_name, "w")

  for currentExecution in range(amountOfExecutions):
    functionTime = getResponseTimeInMillis(getCoffeeImageUrl, scenerie)
    f.write("%d\n"%(functionTime))
    print('Current execution: %d'%(currentExecution))

  f.close()
  print("File '%s' genereted with sucess." %(file_name))