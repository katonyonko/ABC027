import io
import sys

_INPUT = """\
6
M+MM-M
MMM+M
MMM+--MMM
+
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans=[]
  tmp=0
  for i in reversed(range(len(S))):
    if S[i]=='M': ans.append(tmp)
    elif S[i]=='+': tmp+=1
    else: tmp-=1
  ans.sort()
  print(-sum(ans[:len(ans)//2])+sum(ans[len(ans)//2:]))