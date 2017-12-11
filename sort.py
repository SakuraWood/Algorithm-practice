# 冒泡排序
# 思想：两两比较


def bubble_sort(lists):
    v = 0
    length = len(lists)
    for i in range(0, length):
        for j in range(i + 1, length):
            v += 1
            if(lists[i] > lists[j]):
                temp = lists[i]
                lists[i] = lists[j]
                lists[j] = temp
    # print "比较次数：  "+str(v)
    return lists

# 插入排序


def insert_sort(lists):
    v = 0
    length = len(lists)
    for i in range(1, length):
        j = i - 1
        key = lists[i]
        while j >= 0 and lists[j] > key:
            v += 1
            # while j>=0:
            # if(lists[j]>key): 终止条件是遇上前面第一个小的就停止循环，因为之前的都是排好序的
            lists[j + 1] = lists[j]
            lists[j] = key
            j -= 1
    # print "比较次数：  "+str(v)
    return lists

# 希尔排序
# 思想： 增量分组，组内进行直接插入排序


def shell_sort(lists):
    v = 0
    step = 5
    length = len(lists)
    while step >= 1:
        for i in range(step, length):
            j = i - step
            key = lists[i]
            while j >= 0 and lists[j] > key:
                v += 1
                lists[j + step] = lists[j]
                lists[j] = key
                j -= step
        step /= 2
    # print "比较次数：  "+str(v)
    return lists

# 快速排序
# 思想： 通过一趟排序将要排序的数据分割成独立的两部分，
# 其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。


def quick_sort(lists):
    low = 0
    high = len(lists) - 1

    def quick_sort_helper(lists, low, high):
        left = low
        right = high
        key = lists[low]    # 选择第一个元素作为key
        while(left < right):
            while(list[right] >= key and left < right):
                right -= 1
            lists[left] = lists[right]
            while(list[left] <= key and left < right):
                left += 1
            lists[right] = lists[left]
        lists[left] = key
        if(low < left):
            quick_sort_helper(lists, low, left - 1)
        if(high > left):
            quick_sort_helper(lists, left + 1, high)
    quick_sort_helper(lists, low, high)
    return lists

# 直接选择排序
# 基本思想：第1趟，在待排序记录r[1] ~ r[n]中选出最小的记录，将它与r[1]交换；
# 第2趟，在待排序记录r[2] ~ r[n]中选出最小的记录，将它与r[2]交换；
# 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。


def select_sort(lists):
    v = 0
    length = len(lists)
    index = 0
    while(index < length):
        min = index
        for i in range(index, length):
            v += 1
            if(lists[i] < lists[min]):
                min = i
        temp = lists[index]
        lists[index] = lists[min]
        lists[min] = temp
        index += 1
    # print "比较次数：  "+str(v)
    return lists

# 堆排序
# 思想： 建堆的过程是一个不断调整堆的过程


def heap_sort(lists):
    length = len(lists)

    def create_heap(lists, length):
        for i in range(0, length / 2)[::-1]:
            adjust_heap(lists, i, length)

    def adjust_heap(lists, i, length):
        lchild = i * 2 + 1
        rchild = i * 2 + 2
        max = i
        if(lchild < length and lists[max] < lists[lchild]):
            max = lchild
        if(rchild < length and lists[max] < lists[rchild]):
            max = rchild
        if max != i:
            lists[i], lists[max] = lists[max], lists[i]
            adjust_heap(lists, max, length)

    def heap_sort_helper(lists):
        for i in range(0, length)[::-1]:
            lists[0], lists[i] = lists[i], lists[0]
            adjust_heap(lists, 0, i)
    create_heap(lists, length)
    heap_sort_helper(lists)
    return lists

# 归并排序
# 思想： 建立在归并操作上的一种有效的排序算法,
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，
# 得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
# 过程： 比较a[i]和b[j]的大小，若a[i]≤b[j]，则将第一个有序表中的元素a[i]复制到r[k]中，
# 并令i和k分别加上1；否则将第二个有序表中的元素b[j]复制到r[k]中，
# 并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，
# 然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。
# 归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，
# 接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。


def merge_sort(lists):
    def merge(left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


# 基数排序（LSD）
# 思想： 原本的思想是分配10个桶，从数值第0位开始排序，以此类推直到最高位排序完毕。
# 但是，如果这样的话，获取高位的数值会是一个问题，额外的花销可能更大，
# 所以，本着二进制的思想，这里只分配两个桶，即0和1，一切都用移位比较，效率相对较高
# 还有个问题，不知道最大的数是多少位，这个比较难搞，借助一下math函数吧，不然用泰勒展开自己实现一个log函数咯。。。
import math


def radix_sort(lists, radix=2):
    bits = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[]for i in range(radix)]
    index = 0
    while index < bits:
        for i in lists:
            bucket[i >> index & 0x1].append(i)
        del lists[:]
        for j in bucket:
            lists += j
            del j[:]
        index += 1
    return lists


import time


def cal_func_time(string, func, lists):
    # print lists
    start = time.clock()
    func(lists)
    end = time.clock()
    print string + str(end - start)


import random
origin = []
for i in range(5000):
    origin.append(random.randint(0, 10000))
# print list
# origin=[4,2,5,54,23,24,11,3234,3432,56,21,33,663,21,22,33,341,52]
# origin=[16,7,3,20,17,8,19,54,12]
# origin=[12,56,32,17,6,39,25]

list = origin[:]
# print insert_sort(list)
cal_func_time("插入排序耗时：      ", insert_sort, list)

list = origin[:]
# print shell_sort(list)
cal_func_time("希尔排序耗时：      ", shell_sort, list)

list = origin[:]
# print bubble_sort(list)
cal_func_time("冒泡排序耗时：      ", bubble_sort, list)

list = origin[:]
# print quick_sort(list)
cal_func_time("快速排序耗时：      ", quick_sort, list)

list = origin[:]
# print select_sort(list)
cal_func_time("直接选择排序耗时：   ", select_sort, list)

list = origin[:]
# print heap_sort(list)
cal_func_time("堆排序耗时：        ", heap_sort, list)

list = origin[:]
# print merge_sort(list)
cal_func_time("归并排序耗时：      ", merge_sort, list)

list = origin[:]
# print radix_sort(list)
cal_func_time("基数排序耗时：      ", radix_sort, list)
