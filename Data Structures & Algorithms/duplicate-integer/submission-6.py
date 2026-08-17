class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Duplicate=set(nums)
        return False if len(Duplicate)==len(nums) else True
        
        