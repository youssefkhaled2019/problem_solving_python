"""
contest=https://codeforces.com/contest/443/problem/A 
date= Friday, May 19, 2023 
Verdict =Accepted
"""
s=input()
a={'{':"","}":"",",":"" ," ":""}
for i,j in a.items():
    s=s.replace(i,j)

print(len(set(s)))
