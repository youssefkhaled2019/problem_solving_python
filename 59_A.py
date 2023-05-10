"""
contest=  https://codeforces.com/contest/59/problem/A
date= Wednesday, May 10, 2023
Verdict  = Accepted
"""
s=input()
l,u=0,0 #l=lower,upper
for i in s :
    if ("A"<=i<="Z"):
        u+=1
    else:
         l+=1

if(l<u):
  print(s.upper())  
else:
  print(s.lower())
  

