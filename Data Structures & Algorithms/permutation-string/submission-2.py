class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        if l1 > l2:
            return False

        map1, map2 = [0]*26, [0]*26

        for i in range(l1):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1

        if map1 == map2: # initial window
            return True

        for i in range(l2 - l1):
            map2[ord(s2[i]) - ord('a')] -= 1
            map2[ord(s2[i + l1]) - ord('a')] += 1

            if map1 == map2:
                return True

        return False

        