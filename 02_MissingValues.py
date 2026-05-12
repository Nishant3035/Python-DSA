class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original_sum = sum(nums)
        expected_sum = 0
        while n > 0:
            expected_sum = expected_sum+n
            n-=1
        return expected_sum - original_sum
        