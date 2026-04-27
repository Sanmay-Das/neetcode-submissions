class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueMap = {}
        for n in nums:
            if n in uniqueMap:
                return True
            uniqueMap[n] = True
        return False
