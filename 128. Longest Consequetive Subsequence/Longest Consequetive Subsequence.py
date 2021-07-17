def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
          return 0
        nums=list(set(nums))
        nums.sort()
        l,k=[nums[0]],[]
        for i in range(1,len(nums)):
          if nums[i] == (nums[i-1] + 1):
            l.append(nums[i])
          else:
            if len(l)>len(k):
              k=l.copy()
            l=[nums[i]]
        print(l)
        print(k)
        return max(len(k),len(l))
          