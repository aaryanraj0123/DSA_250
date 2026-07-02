class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        prefix = {0:1}
        res = 0
        for n in nums:
            curr += n
            if curr - k in prefix:
                res += prefix[curr - k]
            prefix[curr] = prefix.get(curr, 0) + 1
        return res
