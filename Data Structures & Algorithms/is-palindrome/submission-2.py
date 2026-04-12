class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while j > i:
            while j > i and (not s[j].isalnum()):
                j -= 1

            while i < j and (not s[i].isalnum()):
                i += 1
                
            if j < i:
                return False
            if s[j].lower() == s[i].lower():
                i += 1
                j -= 1
            else:
                return False
            
        return True