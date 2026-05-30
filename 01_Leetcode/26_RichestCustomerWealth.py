class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for customer in accounts:
            wealth=sum(customer)
            maximum=max(wealth,maximum)
        return maximum
