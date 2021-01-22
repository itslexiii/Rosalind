# http://rosalind.info/problems/subs/
# If using finditer in regular expression, only the first overlapped motif would be found.

import re


def getseq():
    fname = input("Please input file location.")
    f = open(fname, 'r').read().split('\n')
    gene = f[0]
    motif = f[1]
    return gene, motif


def find(gene, motif):
    pos = []
    for i in range(len(gene)):
        a = 0
        for j in range(len(motif)):
            if i + len(motif) < len(gene):
                if gene[i + j] == motif[j]:
                    a += 1
                    if a == len(motif):
                        pos.append(i + 1)
    return pos


seq = getseq()
gene = seq[0]
motif = seq[1]
pos = find(gene, motif)
print(*pos)
