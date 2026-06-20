class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0
        maxL = 0

        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
            else:
                left += 1

            maxL = max(maxL, len(s[left:right]))

        return maxL

        