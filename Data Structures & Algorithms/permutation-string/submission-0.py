class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        freq1 = [0]*26

        for char in s1:
            freq1[ord(char) - ord('a')] += 1

        for i in range(len2 - len1 + 1):
            freq2 = [0]*26
            for j in range(len1):
                char = s2[i + j]
                freq2[ord(char) - ord('a')] += 1

            if freq1 == freq2:
                return True

        return False

        
        