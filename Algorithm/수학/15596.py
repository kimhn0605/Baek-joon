# 15596 : 정수 N개의 합

def solve(a) :
  ans = 0
  for i in range(len(a)) :   
    ans += a[i]
  return ans
