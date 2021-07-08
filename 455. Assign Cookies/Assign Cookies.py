import math
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        g.sort()
        s.sort()
        for i in s:
          if len(g)!=0:
            n=g[0]
            if i>=n:
              c=c+1
              g.pop(0)
            
        return c