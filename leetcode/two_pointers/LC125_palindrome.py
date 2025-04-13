class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        left = 0
        right = len(s) - 1
        while (left < right):
            if s[right].isalnum() and s[left].isalnum():
                if s[right] != s[left]:
                    return False
                left += 1
                right -= 1
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))