class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end

        while start <= end:
            mid = (start + end) // 2

            time = sum([math.ceil(pile / mid) for pile in piles])
            
            if time > h:
                start = mid + 1
            else:
                res = min(res, mid)
                end = mid - 1

        return res
        