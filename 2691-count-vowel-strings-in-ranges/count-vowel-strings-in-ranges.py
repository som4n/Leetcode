class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        n = len(words)
        pf = [0]*(n+1)

        vowels = {'a', 'e', 'i', 'o' , 'u'}

        for i in range(n):
            pf[i+1]=pf[i]

            if words [i][0] in vowels and words[i][-1] in vowels:
                pf[i+1]+=1

        ans = []
        for i in queries:
            ans.append ( pf[i[1]+1] - pf[i[0]] )

        return ans

