
class Solution:
    def expand(self, s: str, left: int, right: int) -> str:
        while(left >= 0 and right <= len(s) and s[left] == s[right-1]):
            left -= 1
            right += 1
        return s[left+1:right-1]

    def longestPalindrome(self, s: str) -> str:
        if(len(s) < 2 or s == s[::-1]):
            return s
        ret = ''
        for i in range(len(s)-1):
            sub_s_2wnd = self.expand(s, i, i+1)
            sub_s_3wnd = self.expand(s, i, i+2)
            ret = max(ret, sub_s_2wnd, sub_s_3wnd, key=len)
        return ret

s = Solution()
print(s.longestPalindrome("babad"))
