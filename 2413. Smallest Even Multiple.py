
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res = 0
        for i in range(1,2*n):
            if n % 2 ==0 :
                res = n
            elif n % 2 !=0 :
                res = n * 2
        return res