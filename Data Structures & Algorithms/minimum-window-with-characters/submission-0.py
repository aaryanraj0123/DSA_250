class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        left = 0

        answer = (float('inf'), None, None)

        for right in range(len(s)):

            c = s[right]

            window[c] = window.get(c,0)+1

            if c in need and window[c] == need[c]:
                formed +=1

            while formed == required:

                if right-left+1 < answer[0]:
                    answer = (right-left+1,left,right)

                c = s[left]

                window[c]-=1

                if c in need and window[c] < need[c]:
                    formed -=1

                left +=1

        if answer[0] == float('inf'):
            return ""

        return s[answer[1]:answer[2]+1]
        