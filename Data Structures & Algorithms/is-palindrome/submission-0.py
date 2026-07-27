class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = "".join(c.lower() for c in s if c.isalnum())
        return newstr == newstr[::-1]