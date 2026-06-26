def bs(nums,low,high,target):
    if low > high:
        return -1
    mid = (low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bs(nums,mid+1,high,target)
    else:
        return bs(nums,low,mid-1,target)
    
nums = [2, 4, 6, 8, 10, 12]
target = 10

print(bs(nums, 0, len(nums) - 1, target))