class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) <= 1:
            return [strs]

        map_ = defaultdict(list)

        for string in strs:
            counter = [0]*26

            for char in string:
                counter[ord(char)-97] += 1

            map_[tuple(counter)].append(string)

        return list(map_.values())