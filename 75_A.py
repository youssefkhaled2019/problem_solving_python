"""
contest= https://codeforces.com/contest/75/problem/A
date= Tuesday, May 9, 2023
Verdict  =Accepted
"""
def remove_zero(x): #.replace("0","")
    s=""
    for i in str(x):
        if (i!="0"):
          s+=i
    return int(s)      

a=int(input())
b=int(input())
c=remove_zero(a+b)

a_,b_=remove_zero(a),remove_zero(b)
c_=a_+b_
if (c==c_):
   print("YES")
else:
   print("NO")