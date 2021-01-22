# http://rosalind.info/problems/edit/
# Dynamic programming.

import re
import pandas as pd
import numpy as np


def openf():
    fname = input('Input File Location.')
    f = open(fname, 'r').read().split('>')[1:]
    fs = []
    for i in range(len(f)):
        f[i]=re.search('\D+$', f[i]).group()
        f[i]=f[i].replace('\n', '')
        fs.append(f[i])
    p1 = fs[0]
    p2 = fs[1]
    return p1, p2


def orichess(p1, p2):
    size1 = len(p1)+2
    size2 = len(p2)+2
    chess = []
    for k in range(size2):
        chess.append(k)
    for i in range(size2):  # Row number
        if i == 0:
            chess[i] = []
            chess[i].append('na')
            chess[i].append('na')
            for j in p1:
                chess[i].append(j)
        elif i == 1:
            chess[i] = []
            chess[i].append('na')
            for j in range(size1 - 1):
                chess[i].append(j)
        else:
            chess[i] = []
            chess[i].append(p2[i - 2])
            chess[i].append(i - 1)
            for j in range(size1 - 2):
                chess[i].append(0)
    return chess


def fillchess(p1, p2, chess):
    size1 = len(p1) + 2
    size2 = len(p2) + 2
    for i in range(2, size2):
        for j in range(2, size1):
            if chess[0][j] == chess[i][0]:
                chess[i][j] = chess[i-1][j-1]
            else:
                chess[i][j] = min(chess[i-1][j], chess[i][j-1], chess[i-1][j-1]) + 1
    return chess


p = openf()
p1 = p[0]
p2 = p[1]
chess = orichess(p1, p2)
chessfilled = fillchess(p1, p2, chess)
print(chessfilled[len(p2)+1][len(p1)+1])