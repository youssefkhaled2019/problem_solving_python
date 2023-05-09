"""
contest= https://codeforces.com/contest/263/problem/A
date= Tuesday, May 9, 2023
Verdict  = Accepted
"""
# "000".find("1")
for _i in range (5):
    a=list(map(int,input().split(" ")))
    if (1 in a):
        i=_i
        j=a.index(1)
        break

print(abs(2-i)+abs(2-j)) 
