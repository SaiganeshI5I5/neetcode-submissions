class Solution:
    def isPalindrome(self, s: str) -> bool:
        A = "".join(c.lower() for c in s if c.isalnum())
        return A == A[::-1]