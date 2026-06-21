class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        first = 0
        last = n-1
        while first<last:
            s[first], s[last] = s[last], s[first]
            first+=1
            last-=1