import io
import sys

_INPUT = """\
6
1 1 2
4 3 4
5 5 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  L=list(map(int,input().split()))
  for i in range(3):
    if L.count(L[i])%2==1: print(L[i]);break