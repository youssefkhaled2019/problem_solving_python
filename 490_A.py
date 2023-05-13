"""
contest=  https://codeforces.com/contest/490/problem/A 
date= Saturday, May 13, 2023 
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))
l_1,l_2,l_3=[],[],[]
for i in range(n):
    if (l[i]==1):
         l_1.extend([i+1])
    elif (l[i]==2):
         l_2.extend([i+1])
    elif (l[i]==3):
         l_3.extend([i+1])  
s_1,s_2,s_3=len(l_1),len(l_2),len(l_3)                 
print(min(s_1,min(s_2,s_3)))
for i,j,k in zip(l_1,l_2,l_3):
    print(i,j,k)