class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map_ = defaultdict(int)

        left = 0
        maxf = 0
        res = 0

        for right, char in enumerate(s):
            # window_size = right - left + 1
            map_[char] += 1
            maxf = max(maxf, map_[char])

            while (right - left + 1) - maxf > k:
                map_[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res