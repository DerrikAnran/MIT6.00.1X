# -*- coding: utf-8 -*-

# the "classic" recursive problem   经典递归问题

# factorial 阶乘(递归版本)

def factR(n):
    """
    assumes that n is an int > 0
    returns n!
    """
    if n == 1:
        return 1
    return n * factR(n-1)

# factorial 阶乘(迭代版本)

def fact(n):
    """
    assumes that n is an int > 0
    returns n!
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Tower of Hanoi    将套在一座塔上的一系列直径由上而下递增的套圈，原样转移到另一座塔上的方案
# 理解递归思想的应用，将问题分解为简单版本,列出基线条件(base case)，再利用递归调用，列出递归条件(recursive case)

def printMove(fr, to):
    print "move from", fr, "to", to

def Towers(n, fr, to, spare): # n:套圈数目 fr:起点塔 to:终点塔 spare:空闲塔
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to) # 先把上面的n-1个套圈移到空闲塔上
        Towers(1, fr, to, spare) # 然后把最下面的大套圈移到终点塔上
        Towers(n-1, spare, to, fr) # 最后把空闲塔上的n-1个套圈移到终点塔上

# Fibonacci 多基线条件(base cases)的递归

def fib(x):
    """
    assumes x an int >= 0
    returns Fibonacci of x
    """
    # 断言语句，判断assert后语句的True/False，若True则执行下方语句，若False则报错不执行下方语句
    assert type(x) == int and x >= 0

    if x == 0 or x == 1: # two base cases 两个基线条件，简单版本
        return 1
    else:
        return fib(x-1) + fib(x-2) # recursive case 递归调用

# Recursion on strings # 判断一句话(字符串)是否为回文句
# 理解分而治之(divide and conquer)的思想,即把复杂的问题分解成一系列更易解决的子问题，
# 然后将子问题的解决方案结合起来，解决复杂问题

def isPalindrome(s):

    # 将字符串中字母提取出来并转换为lower case
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijkmnlopqrstuvwxyz':
                ans = ans + c
        return ans

    # 判断处理后的字符串是否为回文句
    def isPal(s):
        if len(s) == 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) # s[1:-1]筛选出判断完首尾后的子串

    return isPal(toChars(s))

# Manipulating on tuples 在元组中使用迭代
# 求出两个正整数的所有约数，并存放在tuple中

def findDivisors(n1, n2):
    """
    assumes n1 and n2 positive ints
    returns tuple containing
    common divisors of n1 and n2
    """
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            divisors = divisors + (i,) # + 重载为连接两个元组的符号，tuple can't + str
    return divisors

#
