class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        n = n // 2
        for key, value in freq.items():
            if value > n:
                return key
        return 0