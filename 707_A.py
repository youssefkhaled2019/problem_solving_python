"""
contest=https://codeforces.com/problemset/problem/707/A
date= Wednesday, June 14, 2023 
Verdict =Accepted
"""
x,y=list(map(int,input().split(" ")))
p="#Black&White"
for i in range(x):
    l=input().split(" ")
    if ('C' in l or 'M' in l or 'Y' in l ):
        p="#Color"
        break

print (p)