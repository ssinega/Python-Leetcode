class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        res = []
        p_count = [0] * 26
        s_count = [0] * 26

        # Count frequency for p and first window in s
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        # Check initial window
        if p_count == s_count:
            res.append(0)

        # Slide the window
        for i in range(len(p), len(s)):
            # add new char
            s_count[ord(s[i]) - ord('a')] += 1
            # remove old char (i - len(p))
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if s_count == p_count:
                res.append(i - len(p) + 1)

        return res
