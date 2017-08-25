
# coding: utf-8

# In[1]:

from random import randint
import random
import time

# 排序算法辅助函数
class SortHelp(object):
    
    def __init__(self):
        pass
    
    # 生成含有n个元素的随机数组
    def generate_rand_list(self, n=10, start=0, stop=10):
        random_list = []
        random_list = [randint(start, stop) for _ in xrange(n)]
        return random_list
    
    # 生成几乎有序的数组
    def gen_nearly_order_list(self, n=10, swaptime=0):
        order_list = range(0,n)
        a = randint(0,n)
        b = randint(0,n)
        temp = order_list[a]
        order_list[a] = order_list[b]
        order_list[b] = temp
        return order_list
        
    
    def test_sort(self, sort_method, test_list):
        start = time.clock()
        sorted_list = sort_method(test_list)
        end = time.clock()
        if self.is_sort(sorted_list) is not True:
            raise(ValueError,"The sorted result is not right!")
        print end - start
    
    def is_sort(self, sorted_list):
        for i in range(1, len(sorted_list)):
            if sorted_list[i] < sorted_list[i-1]:
                return False
        return True
    
sort_help = SortHelp()


# 排序算法
class Sort(object):
    def __int__(self):
        pass
    
    # O(n^2)级排序算法
    # 选择排序算法
    def selection_sort(self, unsort_list):
        rlist = unsort_list
#         min_index = 0
        length = len(rlist)
        for i in range(0, length):
            min_index = i
            for j in range(i+1, length):
                if rlist[j] < rlist[min_index]:
                    min_index = j
            temp = rlist[i]
            rlist[i] = rlist[min_index]
            rlist[min_index] = temp
        return rlist
    
    # 插入排序算法
    # 简易版（内层循环交换三次）
    def insertion_sort(self, unsort_list):
        rlist = unsort_list
        length = len(rlist)
        for i in range(1,length):
            for j in range(i, 0, -1):
                if rlist[j] < rlist[j-1]:
#                     print rlist[j]
                    temp = rlist[j-1]
                    rlist[j-1] = rlist[j]
                    rlist[j] = temp
                else:
                    break
        return rlist
    # 优化版（交换一次）
    def insertion_sort2(self, unsort_list):
        rlist = unsort_list
        length = len(rlist)
        for i in range(1, length):
            e = rlist[i]
#             j = i
#             while j > 0 and rlist[j-1] > e:
#                 rlist[j] = rlist[j-1]
#                 j = j-1
#             rlist[j] = e    
            t = 0
            for j in range(i, 0, -1):
                if rlist[j-1]>e:
                    rlist[j] = rlist[j-1]
                else:
                    t = j
                    break
            rlist[t] = e
        return rlist
    
    # 冒泡排序
    def bubble_sort(self):
        pass
    # 希尔排序
    
    # O(nlogn)级排序算法
    # 归并排序
    def merge_sort(self, unsort_list):
        length = len(unsort_list)
        return self.__merge_sort(unsort_list, 0, length-1)
    
    def __merge_sort(self, unsl, l, r):
        if l>=r:        # 在这里可以实现优化
            return      # 数组比较小的时候可以用插入排序
        rlist = unsl
        mid = (l+r)/2
        self.__merge_sort(rlist, l, mid)
        self.__merge_sort(rlist, mid+1, r)
        if rlist[mid] > rlist[mid+1]:
            self.__merge(rlist, l, mid, r)
        return rlist
        
    def __merge(self, unsort_list, l, mid, r):
        # 此处按C++的方式来，不够Pythonic
        temp_list = [0]*(r-l+1)
        for i in range(l, r+1):
            temp_list[i-l] = unsort_list[i]
        
        # 两个数组的起始点
        i = l
        j = mid+1
        for k in range(l, r+1):
            # 先判断索引的合法性
            if i > mid:
                unsort_list[k] = temp_list[j-l]
                j = j+1
            elif j > r:
                unsort_list[k] = temp_list[i-l]
                i = i+1
            elif temp_list[i-l] > temp_list[j-l]:
                unsort_list[k] = temp_list[j-l]
                j = j+1
            else:
                unsort_list[k] = temp_list[i-l]
                i = i+1
    # 自底向上的归并排序           
    def merge_sort_bu(self, unsorted_list):
        length = len(unsorted_list)
        i = 1
        
        while i <= length:
            j = 0
            while j+i < length:
                if unsorted_list[j+i-1] > unsorted_list[j+i]:
                    self.__merge(unsorted_list, j, j+i-1,min(j+2*i-1, length-1))
                j = j+2*i
            i = i+i
        return unsorted_list
    
    # 快速排序
    # 取第一个值为起始点
    def quick_sort(self, unsort_list):
        length = len(unsort_list)
        self.__quick_sort(unsort_list, 0, length-1)
        return unsort_list
        
    def __quick_sort(self, unsort_list, l, r):
        if l >= r:
            return
        p = self.__partition(unsort_list, l, r)
        self.__quick_sort(unsort_list, l, p-1)
        self.__quick_sort(unsort_list, p+1, r)
    
    def __partition(self, unsort_list, l, r):
        v = unsort_list[l]
        j = l
        for i in range(l+1, r+1):
            if unsort_list[i] < v:
                unsort_list[j+1], unsort_list[i] = unsort_list[i], unsort_list[j+1]
                j = j+1
        unsort_list[j], unsort_list[l] = unsort_list[l], unsort_list[j]
        return j   
    
    # 堆排序
    def heap_sort(self, unsort_list):
        length = len(unsort_list)
        maxheap = MaxHeap()
        for i in range(length):
            maxheap.insert(unsort_list[i])
        for i in range(length-1, -1, -1):
            unsort_list[i] = maxheap.get_max()
        return unsort_list

sort = Sort()            



# 堆数据结构
class MaxHeap(object):
    def __init__(self):
        self.data = [0]
        self.count = 0
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    
    def insert(self, node):
        # 从一开始计数，刚好树的根节点序号和列表位置序号相等
        self.data.append(node)
        self.__shift_up(self.count+1)
        self.count = self.count + 1
        
    def __shift_up(self, k):
        # 当父节点小于子节点时
        while k>1 and self.data[k/2] < self.data[k]:
            self.data[k/2], self.data[k] = self.data[k], self.data[k/2]
            k = k/2
    
    # 取出最大值
    def get_max(self):
        if self.count == 0:
            raise ValueError("错了")
        max = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.__shift_down(1)
        return max
    
    def __shift_down(self, k):
        while 2*k <= self.count:
            j = 2*k
            if j +1 <= self.count and self.data[j+1] > self.data[j]:
                j = j+1
            if self.data[k]>self.data[j]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j
    
            


# 当列表比较有序时，插入排序效率比选择排序更快
# 当然Python内置的排序程序一般是最快的（sorted()）
a = sort_help.generate_rand_list(n=1000, stop=1000)
a_n = sort_help.gen_nearly_order_list(1000, 100)
# print a
import copy

a1 = copy.deepcopy(a_n)
a2 = copy.deepcopy(a_n)
a4 = copy.deepcopy(a_n)
a5 = copy.deepcopy(a_n)
a6 = copy.deepcopy(a_n)
#sort_help.test_sort(sorted, a_n)
#sort_help.test_sort(sort.selection_sort, a_n)
sort_help.test_sort(sort.heap_sort, a1)
#sort_help.test_sort(sort.insertion_sort2, a2)
sort_help.test_sort(sort.merge_sort, a4)
sort_help.test_sort(sort.merge_sort_bu, a5)
sort_help.test_sort(sort.quick_sort, a6)
a3 = sort_help.generate_rand_list()
print a3
print sort.quick_sort(a3)




