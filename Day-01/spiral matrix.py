class Solution:
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Step 1: Traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Step 2: Traverse from top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Step 3: Traverse from right to left (only if still valid)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Step 4: Traverse from bottom to top (only if still valid)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
