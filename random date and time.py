import random
import time 

def getRandomDate(startDate, endDate):
    print("printing random date between", startDate, "and", endDate)
    randomGenerator = random.Random()
    dateFormat = "%m/%d/%Y"
    
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    
    randomTime = startTime + randomGenerator.random() * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    
    return randomDate

print("random date =", getRandomDate("01/01/2016", "12/31/2026"))