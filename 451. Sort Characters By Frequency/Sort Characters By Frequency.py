def frequencySort(self, s: str) -> str:
        s1=list(set(s))
        s1.sort(reverse=True,key=lambda x :s.count(x))
        print(s1)
        s2=""
        for i in s1:
          s2+=i*s.count(i)
        return s2