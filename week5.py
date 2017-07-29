# -*- coding: utf-8 -*-

# Selection sort 选择排序法 O(n**2) 升序排列 先排list头部 小 -----> 大
# 每次内循环找出未排序部分(list尾部)中的最小值加到排序部分(list头部)之后

def selSort(L):
    for i in range(len(L) - 1):
        minIndex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndex = j
                minVal = L[j]
            j += 1
            temp = L[i]
            L[i] = L[minIndex]
            L[minIndex] = temp
    return L


# Bubble sort 冒泡排序法 O(n**2) 升序排列 先排list尾部 小 <----- 大
# 每次内循环把未排序部分(list头部)中的最大值放到排序部分(list尾部)之前

def bulSort(L):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L


# Merge sort 归并排序法 O(nlogn) 升序排列 分而治之，分解成小问题解决

# 归并两个有序列表(left, right), O(len(left)+len(right)) aka O(n)
def merge(left, right, compare):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

# 递归 O(n log n)
import operator
def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
