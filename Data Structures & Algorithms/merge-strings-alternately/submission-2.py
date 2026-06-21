class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        right=0
        result=[]
        while left < len(word1) and right < len(word2):
            result.append(word1[left])
            result.append(word2[right])
            left+=1
            right+=1
        result.append(word1[left:])
        result.append(word2[right:])
        return "".join(result)