'''
Given a number find the number of trailing zeroes in its factorial.
Read input from stdin and provide input before running code

Input Format
A single integer - N

Output Format
Print a single integer which is the number of trailing zeroes.

Input Constraints
1 <= N <= 1000
================================
'''
n=raw_input()
n=int(n)
fact=1
for i in range(1,n+1):
	fact=fact*i
#print fact
numZeros=0
while fact%10==0:
	fact=fact/10
	numZeros=numZeros+1
	
print numZeros
