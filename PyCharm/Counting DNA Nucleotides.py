# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word;
# the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T')
# is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the
# symbols 'A', 'C', 'G', and 'T' occur in s.

def openfile():
    file = open(r'C:\Users\LEXi\Desktop\sample.txt', 'r').read()
    return file


print(openfile())
