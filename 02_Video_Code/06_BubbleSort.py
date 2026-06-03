def BubbleSort(nums):
    n= len(nums)
    for j in range(n-2,-1,-1):
        is_swap=False

        for i in range(0,j+1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                is_swap=True
        if is_swap==False:
            break