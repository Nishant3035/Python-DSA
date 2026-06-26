class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        temp = nums[0]
        for i in range(0,n):
            nums[i] =  nums[(i+1)%n]
        nums[-1]=temp
        return nums