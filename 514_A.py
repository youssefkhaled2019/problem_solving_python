"""
contest=https://codeforces.com/contest/514/problem/A
date= Saturday, June 17, 2023 
Verdict =Accepted
"""

x=list(input())
o=""
for i in range(len(x)):
    s= int(x[i])
    s=str(min(s,9-s))
    o+=  "9" if i==0  and s=="0" else s

print(int(o))