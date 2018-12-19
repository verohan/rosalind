#!/usr/bin/env python

# Rabbits and Recurrence Relations

# Problem
# A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. 
# Sequences can be finite or infinite. Two examples are the finite sequence (π,−2‾√,0,π) and the 
# infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.
# A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. 
# In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive
# the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal
# to the number of rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs
# alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence 
# relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was 
# known to Indian mathematicians over two millennia ago.

# When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation 
# to generate terms for progressively larger values of n. This problem introduces us to the computational technique of 
# dynamic programming, which successively builds up solutions by using the answers to smaller cases.

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation, every pair of reproduction-age 
# rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# Sample Dataset
# 5 3
# Sample Output
# 19

##########################
# Solution from Hazard
##########################
# Solution 1
with open('rosalind_fib.txt', 'r') as f:
    ff=f.readline().strip().split(' ')
    n=int(ff[0]); #  string to int
    k=int(ff[1]);
    F=[0]; # F[0] = 0
    for i in range(0,n):
        if i == 0:
            F.append(1) # F[1] = 1
        else:
            F.append(k*F[-2]+F[-1]) # F[n] = k*F[n-2] + F[n-1]
        
print(F[-1])

# Solution 2: use dynamic programming Recursive call function
def fib(n, k):
    assert n > 0 & k >= 0
    if n == 1 or n == 2:
        return(1)
    else:
        return(fib(n-1, k) + fib(n-2, k)*k)

fib(5, 3)
#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 

######################
# solution from hehan
######################

def fib(n, k):
    if n <= 0:
        return(0)
    elif n == 1:
        return(1)
    else:
        return(fib(n-1,k) + k * fib(n-2,k))
print(fib(5,3))


