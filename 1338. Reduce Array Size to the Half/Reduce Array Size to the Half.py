def minSetSize(self, arr: List[int]) -> int:
      l=list(set(arr))
      if len(l)==len(arr):
        return len(l)//2
      l.sort(reverse=True,key= lambda x: arr.count(x))
      n,c=len(arr),0
      while n>len(arr)//2:
        n=n-arr.count(l[c])
        c=c+1
      return c