class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0

        prefixCount = {0:1}

        for num in nums:

            prefix += num

            if prefix-k in prefixCount:
                count += prefixCount[prefix-k]

            prefixCount[prefix] = prefixCount.get(prefix,0)+1

        return count