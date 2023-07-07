# assign3hackkerquestions.py
https://www.hackerrank.com/challenges/itertools-combinations/problem
This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK


# Enter your code here. Read input from STDIN. Print output to STDOUT
s,k=input().split() 
s=''.join(sorted(s))
s=s.upper()
from itertools import combinations 
for i in range(1,int(k)+1): 
    x=list(combinations(s,i)) 
    for j in x: 
        print(''.join(j))

Input (stdin)
HACK 2
Expected Output
A
C
H
K
AC        

        
