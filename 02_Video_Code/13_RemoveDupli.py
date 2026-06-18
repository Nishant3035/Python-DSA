nums = list(map(int,input().split()))

n = len(nums)
def solve():
    if n == 1:
        return 1
    i = 0
    j = i+1
    while j<n:
        if nums[i] != nums[j]:
            i+=1
            nums[i],nums[j]= nums[j],nums[i]
        j+=1
    return i+1

k= solve()
print(nums[:k])
