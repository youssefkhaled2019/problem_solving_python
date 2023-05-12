"""
contest=  https://codeforces.com/contest/282/problem/A 
date= Friday, May 12, 2023 
Verdict =Accepted
"""
        
n=int(input())
c=0
for i in range(n):
    w=input()
    if ("++"in w):
        c+=1
    elif ("--"in w): 
        c-=1

print(c)