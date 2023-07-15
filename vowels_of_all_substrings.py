class Solution:
    def countVowels(self, word: str) -> int:
        l=len(word)
        res=0
        vow=['a','e','i','o','u']
        for i in range(len(word)):
            if(word[i] in vow):
                res += (l-i)*(i) + (l-i)
        return res    