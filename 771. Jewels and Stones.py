class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        k = 0
        for i in stones :
            if i in jewels:
                k = k+1
        return k