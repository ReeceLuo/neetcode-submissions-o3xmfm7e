class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p2 > p1:
            while p2 > p1 and not s[p1].isalnum():
                p1 += 1
            while p2 > p1 and not s[p2].isalnum():
                p2 -= 1

            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1

        return True