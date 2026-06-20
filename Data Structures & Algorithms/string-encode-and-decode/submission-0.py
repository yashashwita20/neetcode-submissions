class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode = []
        for string in strs:
            encode.append(str(len(string))+'#'+string)
        return ''.join(encode)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decode = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != '#':
                j += 1

            n = int(s[i:j])
            j+=1

            decode.append(s[j : j+n])
            i = j + n

        return decode