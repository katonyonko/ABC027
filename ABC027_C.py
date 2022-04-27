import io
import sys

_INPUT = """\
6
1
5
7
10
123456789123456789
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  a=0
  while N>1:
    if a==0:
      N=N//2
    else:
      if N%2==0:
        N=N//2-1
      else:
        N=N//2
    a^=1
  if N==1:
    if a==0: print('Aoki')
    else: print('Takahashi')
  else:
    if a==0: print('Takahashi')
    else: print('Aoki')