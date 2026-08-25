class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
    
    # Get the k most common elements
        return [item for item, _ in count.most_common(k)]


        