class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        paliCheck = s.replace(' ', '').lower()

        paliCheck = ''.join(char for char in paliCheck if char.isalnum())
        r = len(paliCheck) - 1
        while l < r:
            if paliCheck[l] == paliCheck[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True