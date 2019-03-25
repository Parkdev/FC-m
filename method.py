# utility class (관련기능만 모아놓은 클래스)

# Single responsibility principle
# 통계에 대한 하나의 책임만 진다

import math
from functools import reduce

class Stat:
    def get_average(self, scores):
        '''
        get_average(scores) -> float <2>
        '''
        avg = reduce(lambda a, b: a + b, scores) / len(scores)
        avg = round(avg, 2)
        return avg


    def get_variance(self, scores, avg):
        '''
        get_variacne(scores, avg) -> float <2>
        '''
        var = reduce(lambda res, x: (avg-x)**2 + res, scores, 0) /len(scores)
        var = round(var, 2)
        return var

    def get_std_dev(self, var):
        std_dev = math.sqrt(var)
        return round(std_dev, 2)

# class FileSystem:
#     def read():
#         pass

#     def write():
#         pass

class Reader:
    pass

class Writer:
    pass

class FileSystem:
    def __init__(self):
        self.reader=Reader()
        self.writer=Writer()
