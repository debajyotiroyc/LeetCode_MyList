def findShortestSubArray(self, nums: List[int]) -> int:
      l=list(set(nums))
      l.sort(key=lambda x: nums.count(x),reverse=True)
      n,m=nums.count(l[0]),len(nums)*2
      #print(l)
      #nums=str("".join(map(str,nums)))
      l1=nums[::-1]
      for i in l:
        if n==nums.count(i):
          a,b=nums.index(i),len(l1)-1-l1.index(i)
          if b-a <m:
            m=b-a
        else:
          break
      return m+1