""" 
contest= https://codeforces.com/contest/80/problem/A 
date= Wednesday, May 17, 2023 
Verdict =Accepted
"""
n,m=map(int,input().split())
o=[2,3,5,7]
for i in range(8,55):
  if (i%2!=0 and i%3!=0  and i%5!=0  and i%7!=0  and i%7!=0   ):
   o.extend([i])

if(o[o.index(n)+1]==m):
  print("YES")
else:
  print("NO") 