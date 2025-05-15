class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res=[]
        order=-1
        for i in range(len(groups)):
            if groups[i]!= order:
                order = groups[i]
                res.append(words[i])

        return res