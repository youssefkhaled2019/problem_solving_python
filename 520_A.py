"""
contest=  https://codeforces.com/contest/520/problem/A
date= Sunday, May 14, 2023 
Verdict =Accepted
"""

n=int(input())
s=input().lower()
if(len(set(s))==26):
    print("YES")
else:
    print("NO")    