class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(0,31):
            if n == pow(2,x):
                return True
            x+=1
        return False

def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False
    return n & (n - 1) == 0