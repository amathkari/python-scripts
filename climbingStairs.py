'''
# Read input from stdin and provide input before running code

Alice is climbing stairs. There are total N stairs. She climbs A stairs upwards in day and she comes downstairs in night by B stairs. Find number of days she will take to reach the top of staircase.

Input: 
First and only line contains three space separated integers denoting A, B, N.

Output: 
Print only one line of output denoting the answer to the question.

Constraints: 
1 ≤ B<A≤N ≤ 109

SAMPLE INPUT 
5 1 6
SAMPLE OUTPUT 
2

'''
str1=raw_input()
arr=str1.split(' ')
a=int(arr[0])
b=int(arr[1])
n=int(arr[2])
interval=a-b
#stairs=0
#print n
#print interval
#print n/interval
#print n%interval
days=int(n)/int(interval)
if n%interval>b:
        days=days+1
else:
        days=days-(b/interval)
print days
