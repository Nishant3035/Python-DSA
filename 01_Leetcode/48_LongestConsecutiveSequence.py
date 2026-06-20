class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        nums.sort()

        count = 1
        max_count = 1

        for i in range(n - 1):
            if nums[i + 1] == nums[i]:
                continue

            elif nums[i + 1] == nums[i] + 1:
                count += 1

            else:
                count = 1

            max_count = max(max_count, count)

        return max_count