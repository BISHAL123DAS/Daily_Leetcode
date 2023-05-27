class Solution:
    def climbStairs(self, n: int) -> int:
        i=1
        n2=1
        n3=0
        n1=0
        while i<=n:
            n3=n1+n2
            n1=n2
            n2=n3
            i+=1
          
        return n3