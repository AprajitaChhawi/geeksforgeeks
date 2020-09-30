from itertools import *
try:
    t=int(input())
    while t:
        t=t-1
        s=input()
        l=permutations(s)
        for i in sorted(l):
            print(''.join(i),end=" ")
        print()
except Exception:
    pass;
