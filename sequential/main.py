from sequential_executor import runSceneries

# sceneriesList = [25, 50, 80, 120, 220, 370, 600]
# amountOfExecutions = 22

sceneriesList = [2, 4, 6]
amountOfExecutions = 2

for scenerie in sceneriesList:
  runSceneries(scenerie, amountOfExecutions)