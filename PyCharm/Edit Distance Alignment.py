# http://rosalind.info/problems/edta/

import re
import pandas as pd
import numpy as np


def openfile():
    fname = input('Please input file location.')
    f = open(fname, 'r').read().split('>')[1:]
    p = []
    for i in range(len(f)):
        f[i] = re.search('\D+$', f[i]).group()
        f[i] = f[i].replace('\n', '')
        p.append(f[i])
    p1 = p[0]
    p2 = p[1]
    return p1, p2


def orichess(p1, p2):
    size1 = len(p1) + 2
    size2 = len(p2) + 2
    chess = []
    for k in range(size2):
        chess.append('')
    for i in range(size2):
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


def filledchess(p1, p2, chess):
    size1 = len(p1) + 2
    size2 = len(p2) + 2
    for i in range(2, size2):
        for j in range(2, size1):
            if chess[0][j] == chess[i][0]:
                chess[i][j] = chess[i - 1][j - 1]
            else:
                chess[i][j] = min(chess[i - 1][j], chess[i][j - 1], chess[i - 1][j - 1]) + 1
    return chess


def trace(p1, p2, chess):
    size1 = len(p1) + 2
    size2 = len(p2) + 2
    p1e = ''
    p2e = ''
    i = size2 - 1
    j = size1 - 1
    while i > 1 or j > 1:
        if chess[0][j] == chess[i][0]:
            p1e += chess[0][j]
            p2e += chess[i][0]
            i -= 1
            j -= 1
        elif chess[i][j] == chess[i - 1][j - 1] + 1:
            p1e += chess[0][j]
            p2e += chess[i][0]
            i -= 1
            j -= 1
        elif i <= j:
            if chess[i][j] == chess[i][j - 1] + 1:
                p1e += chess[0][j]
                p2e += '-'
                j -= 1
            elif chess[i][j] == chess[i - 1][j] + 1:
                p1e += '-'
                p2e += chess[i][0]
                i -= 1
        elif i > j:
            if chess[i][j] == chess[i - 1][j] + 1:
                p1e += '-'
                p2e += chess[i][0]
                i -= 1
            elif chess[i][j] == chess[i][j - 1] + 1:
                p1e += chess[0][j]
                p2e += '-'
                j -= 1
    p1e = p1e[::-1]
    p2e = p2e[::-1]
    return p1e, p2e


p = openfile()
p1 = p[0]
p2 = p[1]
chess = orichess(p1, p2)
chess = filledchess(p1, p2, chess)
pe = trace(p1, p2, chess)
p1e = pe[0]
p2e = pe[1]
print(chess[len(p2)+1][len(p1)+1])
print(p1e)
print(p2e)