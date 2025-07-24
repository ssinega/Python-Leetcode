class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # store indices of increasing bars
        max_area = 0
        heights.append(0)  # sentinel to flush stack at the end

        for i, h in enumerate(heights):
            # When current bar is lower than stack top, pop
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
