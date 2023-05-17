"""
contest=https://codeforces.com/contest/785/problem/A
date= Wednesday, May 17, 2023 
Verdict =Accepted
"""
n=int(input())
s=0
z={'Tetrahedron':4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
for i in range(n):
    s+=z.get(input())

print(s)