class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        answer = float('inf')

        for right in range(len(nums)):

            # Expand the window
            current_sum += nums[right]

            # While the window is valid
            while current_sum >= target:

                # Record the current window length
                answer = min(answer, right - left + 1)

                # Shrink the window
                current_sum -= nums[left]
                left += 1

        return 0 if answer == float('inf') else answer
        