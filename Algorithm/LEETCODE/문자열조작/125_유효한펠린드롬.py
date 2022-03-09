class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_list_s = [i.upper() for i in s if(i.isalnum())]
        return to_list_s == to_list_s[::-1]

        
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
