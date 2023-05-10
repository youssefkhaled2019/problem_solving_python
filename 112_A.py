"""
contest=  https://codeforces.com/contest/112/problem/A
date= Wednesday, May 10, 2023
Verdict  = Accepted
"""
a=input().lower()
b=input().lower()
if (a==b):
    print(0)
elif(a<b):
     print(-1)
elif(a>b):
    print(1)
