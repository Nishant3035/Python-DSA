class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map=dict()
        for i in s:
            hash_map[i]=hash_map.get(i,0)+1
        for i in range(len(s)):
            if hash_map[s[i]]==1:
                return i
        return -1
