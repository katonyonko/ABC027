import io
import sys

_INPUT = """\
6
3
1 2 3
5
2 0 0 0 3
2
0 99
4
0 0 0 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  if sum(A)%N!=0: print(-1)
  else:
    n=sum(A)//N
    ans=0
    for i in range(N-1):
      if A[i]!=n:
        ans+=1
        A[i+1]+=A[i]-n
    print(ans)