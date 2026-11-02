class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swapped = False

            for j in range(n - i - 1):

                if nums[j] > nums[j + 1]:

                    # Swap adjacent elements
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

                    swapped = True

            # Already sorted
            if not swapped:
                break

        return nums
