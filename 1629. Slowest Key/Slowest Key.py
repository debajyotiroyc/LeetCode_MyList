 def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        l,m=[],0
        for i in range(len(releaseTimes)):
          if i==0:
            m=releaseTimes[0]
            l=[keysPressed[i]]
            continue
          
          n=releaseTimes[i]-releaseTimes[i-1]
          if n>=m:
            if n==m:
              l.append(keysPressed[i])
            else:
              l=[keysPressed[i]]
              m=n
          
        return max(l)