nums=[5,6,7,7,1,9,10,1,1,5]
hash_map=dict()
n=len(nums)
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map)
