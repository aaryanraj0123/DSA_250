class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   # stores indices
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                right = i
                left = stack[-1] if stack else -1
                width = right - left - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            right = len(heights)
            left = stack[-1] if stack else -1
            width = right - left - 1
            max_area = max(max_area, height * width)

        return max_area