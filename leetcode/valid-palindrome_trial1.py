class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        word = ""
        for i in s:
            if (i>='a' and i<='z') or i>='0' and i<='9':
                word+=i
        return word == word[:: -1]


        
        