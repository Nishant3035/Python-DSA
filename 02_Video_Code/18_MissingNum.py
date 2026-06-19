class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original_sum = sum(nums)
        expected_sum = (n*(n+1))//2
        output = expected_sum - original_sum
        return output