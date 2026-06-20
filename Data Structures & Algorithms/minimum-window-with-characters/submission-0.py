class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0

        t_map = Counter(t)
        w_map = defaultdict(int)
        have = 0
        need = len(t_map) # no of unique characters

        res = ""

        while right < len(s):
            char = s[right]

            w_map[char] += 1

            if char in t_map and w_map[char] == t_map[char]:
                have += 1

            while have == need:
                if (res == "" or right - left + 1 < len(res)):
                    res = s[left:right+1]

                w_map[s[left]] -= 1
                if s[left] in t_map and w_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

            right += 1        

        return res   
        