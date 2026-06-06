def insertionsort(nums):
    n=len(nums)
    for i in range(n):
        key= nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key

nums = [4, 1, 3, 2, 6,8, 5,7]
insertionsort(nums)
print(nums)  # [1, 2, 3, 4, 5, 6]