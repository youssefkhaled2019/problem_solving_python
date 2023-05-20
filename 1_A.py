"""
contest=https://codeforces.com/problemset/problem/1/A
date= Saturday, May 20, 2023 
Verdict =Accepted
"""
a,b,c=map(int,input().split(" "))
print(abs(a//-c)*abs(b//-c))


"""
    import math
     
    n, m, a = map(int, input().split())
     
    num_flagstones = math.ceil(n/a) * math.ceil(m/a)
     
    print(num_flagstones)
"""