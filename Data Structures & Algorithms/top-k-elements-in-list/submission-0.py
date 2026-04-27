class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # Get the k most common elements 
        most_common = count.most_common(k) # Extract just the elements (without their counts) 
        result = [item[0] for item in most_common] 
        return result