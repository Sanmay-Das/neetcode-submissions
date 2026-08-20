# Brute force
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        pairs = list(freq.items())
        pairs.sort(key=lambda x: x[1], reverse=True)
        kelement = []
        for i in range(k):
            kelement.append(pairs[i][0])
        return kelement 
        