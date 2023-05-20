"""
contest=https://codeforces.com/contest/486/problem/A
date=  Saturday, May 20, 2023 
Verdict = Accepted
"""

import math
 
x = int(input())
if x % 2 != 0:
    print(-1 * (math.ceil(x / 2)))
else:
    print(x // 2)



# n=int(input())
# if n%2==0:
#     print(n//2)
# else:
#     print(-(n+1)//2)