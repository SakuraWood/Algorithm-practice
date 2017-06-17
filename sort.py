# 插入排序
def insert_sort(lists):
    length=len(lists)
    for i in range(1,length):
        j=i-1
        key=lists[i]
        while j>=0:
            if(lists[j]>key):
                lists[j+1]=lists[j]
                lists[j]=key
            j-=1
    return lists

# 希尔排序
# 思想： 增量分组，组内进行直接插入排序
def shell_sort(lists):
    step=5
    length=len(lists)
    while step>=1:
        for i in range(step,length):
            j=i-step
            key=lists[i]
            while j>=0:
                if(lists[j]>key):
                    lists[j+step]=lists[j]
                    lists[j]=key
                j-=step
        step/=2
    return lists

# 冒泡排序
# 思想：两两比较
def bubble_sort(lists):
    length=len(lists)
    for i in range(0,length):
        for j in range(i+1,length):
            if(lists[i]>lists[j]):
                temp=lists[i]
                lists[i]=lists[j]
                lists[j]=temp
    return lists

# 快速排序
# 思想： 通过一趟排序将要排序的数据分割成独立的两部分，
# 其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
def quick_sort(lists):
    low= 0
    high=len(lists)-1
    def quick_sort_helper(lists,low,high):
        left=low
        right=high
        key=lists[low]    # 选择第一个元素作为key
        while(left<right):
            while(list[right]>=key and left<right):
                right-=1
            lists[left]=lists[right]
            while(list[left]<=key and left<right):
                left+=1
            lists[right]=lists[left]
        lists[left]=key
        if(low<left):
            quick_sort_helper(lists,low,left-1)
        if(high>left):
            quick_sort_helper(lists,left+1,high)
    quick_sort_helper(lists,low,high)
    return lists

# 基本思想：第1趟，在待排序记录r[1] ~ r[n]中选出最小的记录，将它与r[1]交换；
# 第2趟，在待排序记录r[2] ~ r[n]中选出最小的记录，将它与r[2]交换；
# 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
def select_sort(lists):
    length=len(lists)
    index =0 
    while(index<length):
        min=index
        for i in range(index,length):
            if(lists[i]<lists[min]):
                min=i
        temp=lists[index]
        lists[index]=lists[min]
        lists[min]=temp
        index+=1
    return lists

def heap_sort(lists):
    def create_heap(lists):
        


    
    

list=[4,2,5,54,23,24,11,3234,3432,56,21,33,663,21]
# list=[8,2,6,5,11,7]

# print insert_sort(list)
# print shell_sort(list)
# print bubble_sort(list)
# print quick_sort(list)
print select_sort(list)
