# http://rosalind.info/problems/gc/

import re


def openfile():
    fname = input('Please input file location.')
    f = open(fname, 'r').read()
    f = f.replace('\n', '')
    f = f.split('>')
    f.remove(f[0])
    return f


def getname(f):
    gcname = []
    for i in range(len(f)):
        gcname.append(re.search(r'Rosalind_\d+', f[i]).group())
    return gcname


def countgc(f, gcname):
    gcbp = []
    gccount = []
    for i in range(len(f)):
        gcbp.append(re.search(r'\D+$', f[i]).group())
    for j in range(len(gcbp)):
        gccount.append(((gcbp[j].count('G') + gcbp[j].count('C')) / len(gcbp[j])) * 100)
    return gcname[gccount.index(max(gccount))], max(gccount)


f = openfile()
name = getname(f)
print(countgc(f, name))
