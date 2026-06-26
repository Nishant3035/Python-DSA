nums=list(map(int,input("Enter nums ").split()))
target = int(input("Target "))

def solve():
    n = len(nums)
    for i in range(0,n):
        if nums[i]==target:
            print(i)
            return
    print("Num not found")

solve()