class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = dict()
        n = len(nums)
        for i in range(0,n):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        for key in hash_map:
            if hash_map[key] > n/2:
                return key
