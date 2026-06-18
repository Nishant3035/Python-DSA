nums = list(map(int,input("Nums : ").split()))

n = len(nums)
def solve():
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]= nums[i]
    nums [0] = temp
solve()
print(nums)
