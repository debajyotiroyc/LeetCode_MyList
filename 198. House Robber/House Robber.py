def rob(self, nums: List[int]) -> int:
        l=[0]*len(nums)
        if len(nums)<=2:
          return max(nums)
        elif len(nums)==3:
          return max(nums[1],nums[0]+nums[2])
        else:
          l[0]=nums[0]
          l[1]=nums[1]
          l[2]=nums[2]+l[0]
          
          for i in range(3,len(nums)):
            l[i]=nums[i]+max(l[i-2],l[i-3])
          
          return max(l[-1],l[-2])