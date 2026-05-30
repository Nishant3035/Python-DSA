class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map1=dict()
        hash_map2=dict()
        n=len(s)
        for i in range(0,n):
            hash_map1[s[i]]=hash_map1.get(s[i],0)+1
            hash_map2[t[i]]=hash_map2.get(t[i],0)+1
        if hash_map1 == hash_map2:
            return True
        else:
            return False
