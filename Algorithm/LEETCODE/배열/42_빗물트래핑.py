class Solution:
    def trap(self, height: list[int]) -> int:
        answer = 0
        i = 0
        while i < len(height) - 1:
            if height[i] > 0 and max(height[i+1:]) >= height[i]:
                for j in range(i + 1, len(height)):
                    if height[j] >= height[i]:
                        print(i, j)
                        square = (j - i - 1) * height[j]
                        print(square)
                        for k in range(i + 1, j):
                            square -= height[k]
                        answer += square
                        i = j
                        break 
            i += 1    
        return answer
         
s = Solution()
print(s.trap([4,2,3]))