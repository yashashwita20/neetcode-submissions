class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            while dq and i - dq[0] >= k:
                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            res.append(nums[dq[0]])

        return res