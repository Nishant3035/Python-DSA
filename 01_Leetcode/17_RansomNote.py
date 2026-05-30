class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map= dict()
        for i in magazine:
            hash_map[i]=hash_map.get(i,0)+1
        for char in ransomNote:
            if hash_map.get(char,0)==0:
                return False
            hash_map[char]-=1
        return True