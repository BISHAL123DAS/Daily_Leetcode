class Solution:
    def tribonacci(self, n: int) -> int:
        i=1
        n1=0
        n2=0
        n3=1
        n4=0
        while i<n:
            n4=n1+n2+n3
            n1=n2
            n2=n3
            n3=n4
            i+=1
        return n4    
