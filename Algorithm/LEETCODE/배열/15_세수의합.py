import imp


import itertools

class Solution:
    def threeSum(self, nums):
        answer = []
        for idx in itertools.combinations(range(len(nums)), 3):
            print(idx)
            if nums[idx[0]] + nums[idx[1]] + nums[idx[2]] == 0:
                ret = sorted([nums[idx[0]], nums[idx[1]], nums[idx[2]]])
                if ret not in answer:
                    answer.append(ret)
        return sorted(answer)
        
s = Solution()
s.threeSum([-1,0,1,2,-1,-4])