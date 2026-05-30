class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        highest_candy=0
        for i in candies:
            if i > highest_candy:
                highest_candy=i
        for candy in candies:
            if candy + extraCandies >= highest_candy:
                result.append(True)
            else:
                result.append(False)
        return result