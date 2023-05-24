"""
contest=https://codeforces.com/contest/766/problem/A
date= Wednesday, May 24, 2023 
Verdict =Accepted
"""
a,b = input(),input()
if (a!=b):
    print(max(len(a), len(b)))
  
else:
    print(-1) 

#a,b=input(),input();print([-1,max(len(a),len(b))][a!=b])   
