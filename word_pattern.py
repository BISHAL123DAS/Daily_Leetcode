class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split()
        
        #this line are check for the same len are have this line if not return false.
        if(len(arr)!=len(pattern)):
            return False

        
       # The find() method is used to find the first occurrence of a character in a string, 
       # and the index() method is used to find the first occurrence of an element in a list.
        for i in range(len(arr)): 
            if pattern.find(pattern[i])!=arr.index(arr[i]):
                return False
        return True  