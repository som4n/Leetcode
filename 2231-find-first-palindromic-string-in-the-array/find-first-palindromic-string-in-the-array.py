class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def ispalindrome(word):
            return word == word[::-1]
        ans=''
        for i in words:
            if ispalindrome(i):
                return i
        return ans
        

