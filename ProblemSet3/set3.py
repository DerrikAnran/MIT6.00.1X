# -*- coding: utf-8 -*-

# Problem 1 Radiation exposure 计算某人在某个时间段所接触的辐射量
#           一段时间的辐射量为辐射量对时间的函数f(x)在这段时间内的积分，用宽度为step，
#           高度为f(x)的一系列长方形的面积来近似表示

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    tmp = start
    result = []
    while tmp < stop:
        result.append(step * f(tmp))
        tmp += step
    return sum(result)
