class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        map_ = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for p in s:
            if p in '({[':
                stack.append(p)
                continue

            if stack and map_[p] == stack[-1]:
                stack.pop()
            else:
                return False

        if stack:
            return False

        return True
        