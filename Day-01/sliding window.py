from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # stores indices, not values
        result = []

        for i in range(len(nums)):
            # Step 1: Remove indices outside the window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Step 2: Remove smaller values from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Step 3: Add current index
            dq.append(i)

            # Step 4: Add max for valid window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
