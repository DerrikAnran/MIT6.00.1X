# -*- coding: utf-8 -*-

# 10 -> 2 十进制转二进制，往结果的左边依次加数

"""
print "I'll convert a decimal number into a binary form:"
num = int(raw_input("> "))
result = ''

while abs(num) > 0:
    result = str(num % 2) + result
    num /= 2

if num < 0:
    result = '-' + result

print result
"""

# 穷举法求x开方的结果，误差epsilon，步长step合理

"""
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x: # 穷举结束位置ans <= x
    ans += step
    numGuesses += 1
print("numGuesses =" + str(numGuesses))
if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of " + str(x))
else:
    print(str(ans) + "is close to the square root of " + str(x))
"""

# 二分法求x开方的结果 bisection search


def findRoot(x, power, epsilon):
    """
        对x开power次根号求解ans，精确度为epsilon
        x and epsilpn int or float, power an int.
            epsilon > 0 & power >= 1.
        returns a float ans, ans ** power is within epsilon of x.
        if such a float does not exist, it returns None.
    """

    # can't find even powered root of negative number,负数无法开偶数次根
    if x < 0 and power % 2 == 0:
        return None

    # low = 0   -> low = min(0,x)   -> low = min(-1,x)
    # high = x  -> high = max(0,x)  -> high = max(1,x)
    # x >= 1       x<=-1 or x>=1       suit for all number x
    low = min(-1, x) # 下界
    high = max(1, x) # 上界

    ans = (low + high) / 2.0
    while abs(ans**power - x) > epsilon:
        if ans ** power > x:
            high = ans
        else:
            low = ans
        ans = (high + low) / 2.0
    return ans


# 二分法查找0-100中某个数，按提示输入low/high判断上下界

"""
print "Please think of a number between 0 and 100!"
ans = 'l'
low = 0
high = 100
ans_number = (low + high) / 2
while ans != 'c':
    print "Is your secret number " + str(ans_number) + "?"
    print "Enter 'h' to indicate the guess is too high. ",
    print "Enter 'l' to indicate the guess is too low. ",
    print "Enter 'c' to indicate I guessed correctly. ",
    ans = raw_input()
    if ans == 'l':
        low = ans_number
    elif ans == 'h':
        high = ans_number
    elif ans == 'c':
        print "Game over. Your secret number was: " + str(ans_number)
        break
    else:
        print "Sorry, I did not understand your input."
        continue
    ans_number = (high + low) / 2
"""

# Newton-Raphson 算法

"""
epsilon = 0.01
y = 24.0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y) / (2*guess))
    print guess
print "Square root of", y, "is about", guess
"""
