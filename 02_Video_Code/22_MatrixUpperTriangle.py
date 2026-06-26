nums = []
for i in range(3):
    row = list(map(int, input().split()))
    nums.append(row)
def solve():
    rows= len(nums)
    cols= len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if j>=i:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
solve()


"""arr = list(map(int, input().split()))

nums = [
    arr[0:3],
    arr[3:6],
    arr[6:9]
]

"""