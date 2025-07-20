from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split()+s2.split())
        res =[]

        for word in count :
            if count[word] == 1:
                res.append(word)
        return res