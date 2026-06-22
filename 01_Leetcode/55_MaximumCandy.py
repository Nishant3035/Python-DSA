class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs) 
        count = 0 
        for i in range(n):
            if costs[i] <= coins:
                coins -= costs[i]
                count += 1
        return count