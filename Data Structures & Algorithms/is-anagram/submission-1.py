class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        map_s = Counter(s)

        for char in t:
            if char not in map_s or map_s[char] == 0:
                return False
            else:
                map_s[char] -= 1

        return True

        