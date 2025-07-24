class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            # Count the current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Track the max frequency character in the window
            max_freq = max(max_freq, count[s[right]])

            # Check if window is invalid (needs > k replacements)
            if (right - left + 1) - max_freq > k:
                # Shrink from left
                count[s[left]] -= 1
                left += 1

            # Update result with valid window size
            result = max(result, right - left + 1)

        return result
