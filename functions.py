from openpyxl import load_workbook
from functools import reduce
import math


def get_raw_data(filename):
    raw_data = {}
    wb = load_workbook(filename)
    ws = wb.active
    g = ws.rows
    for name_cell, scroll_cell in g:
        raw_data[name_cell.value] = scroll_cell.value
    return raw_data
def get_scores(raw_data):
    '''
    get_raw_data(filename) -> dict
    dict = {'name': score1, 'name2': score2, ...}
    '''
    scores = tuple(raw_data.values())
    return scores

def get_average(scores):
    '''
    get_average(scores) -> float <2>
    '''
    avg = reduce(lambda a, b: a + b, scores) / len(scores)
    avg = round(avg, 2)
    return avg


def get_variance(scores, avg):
    '''
    get_variacne(scores, avg) -> float <2>
    '''
    var = reduce(lambda res, x: (avg-x)**2 + res, scores, 0) /len(scores)
    var = round(var, 2)
    return var

def get_std_dev(var):
    std_dev = math.sqrt(var)
    std_dev = round(std_dev, 2)
    return std_dev

def get_evaluation(avg, var, std_dev, sd=20):
    print("평균:{}, 분산:{}, 표준편차:{}".format(avg, var, std_dev))

    if avg < 50 and std_dev > 20:
        print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
    elif avg > 50 and std_dev > 20:
        print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
    elif avg < 50 and std_dev < 20:
        print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
    elif avg > 50 and std_dev < 20:
        print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')

if __name__=="__main__":
    filename = 'class_1.xlsx'
    raw_data = get_raw_data(filename)
    scores = get_scores(raw_data)
    avg = get_average(scores)
    var = get_variance(scores, avg)
    std_dev = get_std_dev(var)
    get_evaluation(avg, var, std_dev)