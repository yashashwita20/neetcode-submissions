class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) <= 1:
            return [strs]

        map_ = defaultdict(list)

        for word in strs:
            count_key = [0] * 26
            
            for char in word:
                count_key[ord(char) - 97] += 1

            map_[tuple(count_key)].append(word)

        return list(map_.values())