import time
import random

testList = [random.randint(1,10000) for i in range(10000)]
# 希尔排序
def hillSort(gap, test_list, llen):
    if gap == 0:
        return test_list
    for i in range(gap):
        cur_idx = i
        cursor = cur_idx + gap
        while cursor <= llen-1:
            while cursor >= gap:
                # 后一个元素比前一个元素小，两个元素交换位置，游标向前移动一位
                if test_list[cursor] < test_list[cursor-gap]:
                    test_list[cursor], test_list[cursor-gap] = test_list[cursor-gap], test_list[cursor]
                    cursor = cursor-gap
                else:
                    break
            cur_idx = cur_idx + gap
            cursor = cur_idx + gap
    return hillSort(gap//2, test_list, llen)

startTime = time.time()
print(hillSort(4, testList, len(testList)))
endTime = time.time()
print('排序使用时间：%s' % (endTime-startTime))