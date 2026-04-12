class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while j > i:
            if s[j].isalnum() and s[i].isalnum():
                if s[j].lower() == s[i].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif s[i].isalnum():
                j -= 1
            else:
                i += 1
            
        return True