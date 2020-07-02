import time
import random
testList = [random.randint(1, 10000) for i in range(10000)]
# testList = [i for i in range(10000)]

# 快排
def quickRow(test_list):
    if len(test_list) <= 1:
        return test_list
    prev = []
    next = []
    middle = []
    for item in test_list:
        if item < test_list[-1]:
            prev.append(item)
        elif item == test_list[-1]:
            middle.append(item)
        else:
            next.append(item)
    return quickRow(prev) + middle + quickRow(next)

startTiem = time.time()
print(quickRow(testList))
endTime = time.time()
print('排序消耗时间： %s' % (endTime-startTiem))