nums1 = list(map(int,input("Num1: ").split()))
nums2 = list(map(int,input("Num2: ").split()))
result = []
n,m=len(nums1),len(nums2)
def solve(nums1,nums2):
    i,j = 0,0
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1

    while i < n:
        if result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    while j < m:
        if result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

solve(nums1,nums2)
print(result)
