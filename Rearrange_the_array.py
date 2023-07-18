class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        possitive=0
        negative=1
        # Define array for storing the ans separately.
        ans = [0]*l
        for i in range(l):
            if(nums[i]<0):
                ans[negative]=nums[i]
                negative+=2
            else:
                ans[possitive]=nums[i]
                possitive+=2

        return ans 