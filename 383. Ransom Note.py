from collections import Counter 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for c in ransom_counter:
            if ransom_counter[c] > magazine_counter[c]:
                return False
        return True