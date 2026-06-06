def largest(nums):
    n=len(nums)
    curr_largest = nums[0]
    for i in range(1,n):
        
        curr_largest = max(curr_largest,nums[i])
        return curr_largest
        
    



nums = [55,32,-97,99,3,67]

