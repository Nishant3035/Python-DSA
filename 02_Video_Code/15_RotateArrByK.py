nums = list(map(int, input("Nums : ").split()))
k = int(input("Enter k: "))

def solve(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]

solve(nums, k)
print(nums)