# http://rosalind.info/problems/cons/

import numpy as np
import pandas as pd
import re


def openfile():
    fname = input('Please input file location.')
    f = open(fname, 'r').read().split('>')[1:]
    seq = []
    for i in range(len(f)):
        f[i] = re.search(r'\D+$', f[i]).group()
        f[i] = f[i].replace('\n', '')
        seq.append(f[i])
    return seq


def matrix(seq):
    S = []
    for i in seq:
        s = []
        for j in i:
            s.append(j)
        S.append(s)
    matrixA = pd.DataFrame(S)
    return matrixA


def countbp(seq, matrixA):
    profile = []
    for j in range(len(seq[0])):
        A = 0
        C = 0
        G = 0
        T = 0
        profiles = []
        for i in range(len(seq)):
            ij = matrixA.iloc[i, j]
            if ij == 'A':
                A += 1
            elif ij == 'C':
                C += 1
            elif ij == 'G':
                G += 1
            elif ij == 'T':
                T += 1
        profiles.append(A)
        profiles.append(C)
        profiles.append(G)
        profiles.append(T)
        profile.append(profiles)
    matrixB = pd.DataFrame(profile).T
    matrixB.index = ['A', 'C', 'G', 'T']
    return matrixB


def ancestor(seq, matrixB):
    cs = ''
    for j in range(len(seq[0])):
        for i in range(4):
            if matrixB.iloc[i,j] == max(matrixB[j]):
                cs += matrixB.index[i]
                break
    return cs


seq = openfile()
matrixA = matrix(seq)
matrixB = countbp(seq, matrixA)
cs = ancestor(seq, matrixB)

print(cs)
print('A:', *matrixB.values[0])
print('C:', *matrixB.values[1])
print('G:', *matrixB.values[2])
print('T:', *matrixB.values[3])

