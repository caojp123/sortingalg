import time
import random

testList = [random.randint(1, 10000) for i in range(10000)]

# 归并排序
def mergeSort(test_list):
    # 拆分
    middle_idx = len(test_list)//2
    left_list = test_list[:middle_idx]
    right_list = test_list[middle_idx:]

    if len(left_list) != 1:
        left_list = mergeSort(left_list)
    if len(right_list) != 1:
        right_list = mergeSort(right_list)

    left_cursor = 0
    right_cursor = 0
    result_list = []

    while True:
        if left_list[left_cursor] > right_list[right_cursor]:
            result_list.append(right_list[right_cursor])
            right_cursor += 1
            if right_cursor >= len(right_list):
                result_list.extend(left_list[left_cursor:])
                break
        else:
            result_list.append(left_list[left_cursor])
            left_cursor += 1
            if left_cursor >= len(left_list):
                result_list.extend(right_list[right_cursor:])
                break
    return result_list

startTime = time.time()
mergeSort(testList)
middleTime = time.time()
print('排序消耗时间：%s' % (middleTime-startTime))
testList = [random.randint(1, 10000) for j in range(100000)]
startTime = time.time()
sorted(testList)
endTime = time.time()
print('排序消耗时间：%s' % (endTime-startTime))
