def palindrome(s,left,right):
    if left >= right:
        return True
    if s[left]!=s[right]:
        return False
    return palindrome(left+1,right-1)
    