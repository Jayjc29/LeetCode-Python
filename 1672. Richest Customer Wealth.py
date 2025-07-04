class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            if wealth> res :
                res = wealth
        return res