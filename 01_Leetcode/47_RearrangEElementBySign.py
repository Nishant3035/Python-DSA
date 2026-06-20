class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result = [0]*n
        p_idx,n_idx=0,1

        for i in range(0,n):
            if nums[i]>=0:
                result[p_idx] = nums[i]
                p_idx+=2
            else:
                result[n_idx]=nums[i]
                n_idx+=2
        return result
