n = int(input())
nums = []
for i in range(n):
    row = list(map(int, input().split()))
    nums.append(row)
def solve():
    row = len(nums)
    col = len(nums[0])
    for i in range(0,row):
        for j in range(0,col):
            if i==j:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
solve()