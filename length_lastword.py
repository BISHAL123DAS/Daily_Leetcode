class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arrs=s.split()
        return len(arrs[-1])