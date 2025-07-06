class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        n = extraCandies
        max_candies= candies[0]
        for candy in candies:
            if candy > max_candies :
                max_candies = candy 
        
        for candy in candies :
            if candy + n >= max_candies:
                res.append(True)
            
            else:
                res.append(False)
        return res