"""
contest=  https://codeforces.com/contest/556/problem/A 
date=Friday, May 12, 2023
Verdict =Accepted
"""
n=int(input())
s=input()
c_0=s.count("0")
c_1=s.count("1")
print(len(s)-min(c_0,c_1)*2)