# -*- coding: utf-8 -*-

from sys import argv
s = argv[1]

# Problem 1 : Counting vowels 统计一个字符串(默认小写)中元音字母的数量 ----- in

count1 = 0
for i in s:
    if i in ('a', 'e', 'i', 'o', 'u'):
        count1 += 1
print "Number of vowels:", count1

# Problem 2 : Counting bobs 统计字符串中'bob'出现的次数(可重叠) ----- 切片

count2 = 0
for i in range(len(s) - 2):
    if s[i:i+3] == 'bob':
        count2 += 1
print "Number of times bob occurs is:", count2

# Problem 3 : Alphabetical substrings 找出字符串中最长的按字母顺序排列的片段 ----- loop & if
# 思路：先将字符串分为若干个按字母顺序排序的片段，然后找出最长的那个并打印(长度相同的打印先出现的)

i = 0
strings = [] # 所有片段存在strings中
while i < len(s): # 外层循环控制片段的起始位置
    tmp = '' # 单个片段存在tmp中
    tmp += s[i]
    j = i
    while j < len(s): # 内层循环决定片段的长度
        if j + 1 < len(s) and s[j+1] >= s[j]:
            tmp += s[j+1]
            j += 1
        else:
            j += 1
            i = j
            strings.append(tmp)
            break
result = strings[0]
for i in strings:
    if len(i) > len(result):
        result = i
print "Longest substring in alphabetical order is:", result
