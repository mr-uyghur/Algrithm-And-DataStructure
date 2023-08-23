class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return(list(set(nums)))
    
print(Solution().removeDuplicates([1,1,2]))