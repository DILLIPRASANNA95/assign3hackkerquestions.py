from itertools import combinations
print(list(combinations("12345",4,)))
print()

s,k=input().split() 
s=''.join(sorted(s))
s=s.upper()
from itertools import combinations 
for i in range(1,int(k)+1): 
    x=list(combinations(s,i)) 
    for j in x: 
        print(''.join(j))
