import time
import random
testList = [random.randint(1,10000) for i in range(10000)]
resultList = [testList[0]]
startTime = time.time()
for i in range(1,len(testList)):
    for j in range(len(resultList)-1,-1,-1):
        if testList[i] < resultList[j]:
            pass
        else:
            resultList.insert(j+1,testList[i])
            break
    else:
        resultList.insert(0,testList[i])
endTime = time.time()
print('排序消耗时间：%s' % (endTime-startTime))
print(resultList)