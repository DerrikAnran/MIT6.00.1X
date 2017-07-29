# -*- coding: utf-8 -*-

def creditCardPayment1(a, monthlyPaymentRate, annualInterestRate):
    """
    Problem 1 Paying the minimum
      计算信用卡的还款人每月按最低还款额还款一年后的余额
      a = balance = unpaidbalance(lastMonth) + interest(lastMonth)
      b = unpaidbalance = balance - minimumPayment
      c = minimumPayment = balance * monthlyPaymentRate
      d = interest = unpaidbalance * annualInterestRate / 12.0
    """
    totalPayment = 0
    for i in range(1, 13):
        c = a * monthlyPaymentRate
        b = a - c
        d = b * annualInterestRate / 12.0
        a = b + d
        totalPayment += c
        print "Month:", i
        print "Minimum monthly payment: %.2f" % c
        print "Remaining balance: %.2f" % a
    print "Total paid: %.2f" % totalPayment
    print "Remaining balance: %.2f" % a


def creditCardPayment2(a, annualInterestRate):
    """
    Problem 2 Paying debt off in a year
      计算信用卡的还款人每月需还款数，使得1年后还清款项，每月还款为10的倍数
      a = balance = unpaidbalance(lastMonth) + interest(lastMonth)
      b = unpaidbalance = balance - minimumPayment
      c = minimumPayment => 输出结果
      d = interest = unpaidbalance * annualInterestRate / 12.0
    """
    c = 0
    tmp = a
    while tmp > 0 and c < a:
        tmp = a
        for i in range(1, 13):
            b = tmp - c
            d = b * annualInterestRate / 12.0
            tmp = b + d
        c += 10
    print "Lowest Payment:", c - 10


def creditCardPayment3(a, annualInterestRate):
    """
    Problem 3 Using bisection search to make the program(problem2 above) faster
      计算信用卡的还款人每月需还款数，使得1年后还清款项，用二分法更加精确快速的计算还款数
      a = balance = unpaidbalance(lastMonth) + interest(lastMonth)
      b = unpaidbalance = balance - minimumPayment
      c = minimumPayment => 输出结果
      d = interest = unpaidbalance * annualInterestRate / 12.0
    """
    low = 0
    high = a
    c = (low + high) / 2.0
    epsilon = 0.01
    tmp = a
    while abs(tmp) > epsilon:
        tmp = a
        for i in range(1, 13):
            b = tmp - c
            d = b * annualInterestRate / 12.0
            tmp = b + d
        if tmp > 0:
            low = c
        elif tmp < 0:
            high = c
        c = (low + high) / 2.0
    print "Lowest Payment: %.2f" % c
