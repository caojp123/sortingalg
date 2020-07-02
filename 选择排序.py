import time
import random

testList = [random.randint(1,10000) for i in range(10000)]
startTime = time.time()
for i in range(len(testList)-1):
    for j in range(i+1, len(testList)):
        if testList[i] > testList[j]:
            testList[i],testList[j] = testList[j],testList[i]
endTime = time.time()
print('排序时间为： %s' % (endTime-startTime))
排序算法