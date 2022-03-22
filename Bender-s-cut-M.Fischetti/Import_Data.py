import numpy as np
from io import StringIO
import gurobipy as gp
from gurobipy import GRB

def import_by_name(name):
    data = []
    path = './Data/'


    c_found = 0
    d_found = 0
    count = -1
    for line in open(path + name):
        data.append(
            np.genfromtxt(StringIO(line.replace('\n', '')),
                          delimiter='\t',
                          dtype=str))
        if c_found == 0:
            if np.genfromtxt(StringIO(line.replace('\n', '')),
                             delimiter='\t',
                             dtype=str)[0] == '-1e30':
                index_c = count
                c_found = 1
        else:
            pass
        if d_found == 0:
            if np.genfromtxt(StringIO(line.replace('\n', '')),
                             delimiter='\t',
                             dtype=str)[0] == '0.001':
                index_d = count
                d_found = 1
        else:
            pass
        if c_found + d_found == 2:
            pass
        else:
            count += 1
    #读取并标定c,d变量的位置


    number_of_continuous = int(data[0][0])
    number_of_row = int(data[0][1])
    begin_index_of_inequality = int(data[0][0]) + 1
    end_index_of_inequality = begin_index_of_inequality + int(data[0][1])


    A = np.zeros(
        (number_of_row, number_of_continuous))
    #系数矩阵A
    a = np.zeros((1, number_of_continuous))
    a[0, index_d] = -1

    #变量d的系数a

    e1 = np.delete(np.eye(number_of_continuous), [index_c, index_d], axis=0)
    e2 = np.delete(-np.eye(number_of_continuous), [index_c, index_d], axis=0)

    #对于w的范围约束系数矩阵e1,e2


    for i in range(begin_index_of_inequality, end_index_of_inequality):
        for j in range(1, int(data[i][0]) + 1):
            A[i - begin_index_of_inequality,
              int(data[i][2 * j + 1])] = float(data[i][2 * j + 2])
    A = np.r_[A, e1, e2, a]
    #合并A得到最终系数矩阵
    return A, number_of_row, number_of_continuous

