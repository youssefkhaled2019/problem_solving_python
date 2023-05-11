"""
contest=  https://codeforces.com/contest/731/problem/A
date= Thursday, May 11, 2023
Verdict = Accepted
"""
w='a'+input()
x=0
for i in range(len(w)-1):
    tem_1= abs((ord(w[i])%ord('a') ) -(ord(w[i+1])%ord('a') ))
    tem_2= abs(tem_1-26)
    x+= min (tem_1 , tem_2 )
print(x)