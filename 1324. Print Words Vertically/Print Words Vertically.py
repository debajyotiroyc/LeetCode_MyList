def printVertically(self, s: str) -> List[str]:
        l=s.split()
        n=len(max(l,key=len))
        j=0
        word=[""]*n
        while j<n:
          for i in range(0,len(l)):
            if j<len(l[i]):
              word[j]=word[j]+l[i][j]
            else:
              word[j]=word[j]+" "
          k=len(word[j])
          for i in range(len(word[j])-1,-1,-1):
            if word[j][i].isspace():
              k=k-1
            else:
              break
          word[j]=word[j][:k]
          j=j+1
        return word