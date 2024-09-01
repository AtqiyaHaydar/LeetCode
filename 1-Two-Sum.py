class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        found = False

        l = 0

        while l < len(nums) and not found:
            for i in range(l + 1, len(nums)):
                if nums[l] + nums[i] == target:
                    res.append(l)
                    res.append(i)
                    found = True
                    break
                else:
                    continue
            
            l = l + 1

        return res