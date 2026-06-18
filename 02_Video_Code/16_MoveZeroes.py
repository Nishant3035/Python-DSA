nums = list(map(int,input("Nums : ").split()))
n =  len(nums)

def solve(nums):
    left = 0
    for i in range(0,n):
        if nums [i] != 0:
            nums[left],nums[i]= nums[i],nums[left]
            left+=1

solve(nums)
print(nums)