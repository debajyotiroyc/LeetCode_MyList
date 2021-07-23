class Solution:
    d={0:0,1:1,2:2,3:3}
    def climbStairs(self, n: int) -> int:
      if n in self.d.keys():
        return self.d[n]
      else:
        self.d[n]=self.climbStairs(n-2)+self.climbStairs(n-1)
      return self.d[n]
    
