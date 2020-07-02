import time
import random

testList = [random.randint(1,10000) for i in range(10000)]
# testList = [i for i in range(10000)]
print(testList)
startTime = time.time()
for i in range(len(testList)-1):
    for j in range(len(testList)-i-1):
        if testList[j] > testList [j+1]:
            testList[j], testList[j+1] = testList[j+1], testList[j]
endTime = time.time()
print('排序时间为： %s' % (endTime-startTime))
