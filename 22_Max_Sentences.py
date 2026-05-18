class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_sen=0
        for i in sentences:
            sen=len(i.split())
            if sen>max_sen:
                max_sen=sen
        return max_sen