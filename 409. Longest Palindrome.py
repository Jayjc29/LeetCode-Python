from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count= Counter(s)
        length = 0
        odd_found = False

        for char,freq in count.items():
            if freq % 2 == 0 :
                length = length+freq
            else :
                length = length +freq -1 
                odd_found = True
        
        if odd_found:
            length +=1
        return length