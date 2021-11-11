def addRungs(self, rungs: List[int], dist: int) -> int:
      k,a=0,0
      i=0
      while i<len(rungs):
        if (rungs[i]-a)<=dist:
          pass
        else:
          if (rungs[i]-a)%dist==0:
            k=k+((rungs[i]-a)//dist)-1
          else:
            k=k+((rungs[i]-a)//dist)
        a=rungs[i]
        i=i+1
      return k
          