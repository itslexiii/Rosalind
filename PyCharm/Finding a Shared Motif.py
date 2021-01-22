# http://rosalind.info/problems/lcsm/
# Classic longest common substring problem.

import re


def openfile():
    fname = input('Please input file location.')
    gf = open(fname, 'r').read().split('>')[1:]
    gfbp = []
    for i in range(len(gf)):
        seq = re.search(r'\D+$', gf[i]).group()
        seq = seq.replace('\n', '')
        gfbp.append(seq)
        gfbp = sorted(gfbp, key=len)
    return gfbp


# Open file and create a list of pure sequence (sorted with length).


def getcom(gfbp):
    x1 = gfbp[0]
    x2 = gfbp[1]
    com = []
    for i in range(len(x2)):
        for k in range(len(x1)):
            st = ''
            for j in range(len(x1)):
                if i + j >= len(x2) or k + j >= len(x1):
                    break
                elif x1[k + j] != x2[i + j]:
                    if len(st) > 10 and st not in com:
                        com.append(st)
                    break
                elif x1[k + j] == x2[i + j]:
                    st += x1[k + j]
                    if len(st) > 10 and st not in com:
                        com.append(st)
    return com


# Get all common subsequences between the shortest two sequences.


def getallcom(gfbp, com):
    comcom = []
    for i in com:
        x = 0
        for j in gfbp:
            if i in j:
                x = x + 1
            if x == len(gfbp) and i not in comcom:
                comcom.append(i)
    comcom = sorted(comcom, key=len)
    return comcom


# Get the common subsequences in all sequences, the list sorted with length.


gfbp = openfile()
com = getcom(gfbp)
comcom = getallcom(gfbp, com)
print(comcom[-1])  # Print out the longest common substring.
