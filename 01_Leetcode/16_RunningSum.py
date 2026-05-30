class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum=0
        n=len(nums)
        for i in range(0,n):
            curr_sum+=nums[i]
            nums[i]=curr_sum

        return nums

        