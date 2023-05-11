"""
contest=  https://codeforces.com/contest/344/problem/A
date= Thursday, May 11, 2023
Verdict =Accepted
"""
n =int(input())
s=""
for i in range(n):
    s+=input()
print(s.count("00")+s.count("11")+1)  