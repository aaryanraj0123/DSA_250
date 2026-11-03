class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero = one = two = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[two] = 2
        #         nums[one] = 1
        #         nums[zero] = 0
        #         two += 1
        #         one += 1
        #         zero += 1
        #     elif nums[i] == 1:
        #         nums[two] = 2
        #         nums[one] = 1
        #         two += 1
        #         one += 1
        #     else:
        #         nums[two] = 2
        #         two += 1

        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] >= nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums