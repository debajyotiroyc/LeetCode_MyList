def lemonadeChange(self, bills: List[int]) -> bool:
        d=dict()
        d[5]=0
        d[10]=0
        i=0
        while i<len(bills):
          if i==0 and bills[i]!=5:
            return False
          if bills[i]==5:
            d[5]+=1
          elif bills[i]==10 and d[5]<1:
            return False
          elif bills[i]==20:
            if d[5]>=1 and d[10]>=1:
              d[10]-=1
              d[5]-=1
            elif d[5]>=3:
              d[5]-=3
            else:
              return False
            
          else:
            d[5]-=1
            d[10]+=1
          i=i+1
        return True    