class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        for j in range(i, n):
            if nums[j] == 1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1