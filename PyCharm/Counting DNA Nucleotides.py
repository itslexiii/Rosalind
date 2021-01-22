# http://rosalind.info/problems/dna/

def openfile():
    file = open(r'C:\Users\LEXi\Desktop\sample.txt', 'r').read()
    return file


def countDNA(string):
    a = 0
    g = 0
    c = 0
    t = 0
    for i in string:
        if i == 'A':
            a += 1
        elif i == 'G':
            g += 1
        elif i == 'C':
            c += 1
        elif i == 'T':
            t += 1
    return a, g, c, t


st = openfile()
print(countDNA(st))
