#!/usr/bin/env python

# Counting DNA Nucleotides

# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; 
# the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 20 12 17 21

##########################
# Solution from Hazard
##########################
# Solution 1
s='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
aa=cc=gg=tt=0
for i in s:
  if i=='A':
    aa += 1
  elif i == 'C':
    cc += 1
  elif i == 'G':
    gg += 1
  elif i == 'T':
    tt += 1
  else:
    continue

print(aa,cc,gg,tt)

# Solution 2: use Python String count() Method 
s='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))

# Solution 3: use Counter from collections
from collections import Counter
s='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
sc=Counter(s)
print(sc['A'], sc['C'], sc['G'], sc['T'])

#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 

################################
# Solution from Hehan 2018-12-11
################################
txt = 'GCCTAAGGGTAGGGCGGCAGCAAGGAAGGGGGCA'
a = 0
t = 0
c = 0
g = 0
for i in txt:
    if i == 'A':
        a += 1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1
    elif i == 'T':
        t += 1
print(a,c,g,t)
