# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         m = max(people)
#         count = [0] * (m + 1)
#         for p in people:
#             count[p] += 1

#         idx, i = 0, 1
#         while idx < len(people):
#             while count[i] == 0:
#                 i += 1
#             people[idx] = i
#             count[i] -= 1
#             idx += 1

#         res, l, r = 0, 0, len(people) - 1
#         while l <= r:
#             remain = limit - people[r]
#             r -= 1
#             res += 1
#             if l <= r and remain >= people[l]:
#                 l += 1
#         return res

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = [0 for i in range(limit+1)]
        result = 0
        for p in people:
            count[p] += 1
        

        left = 1
        right = limit

        while left < right:
            
            leftCount = count[left]
            if leftCount == 0:
                left+=1
                continue
            rightCount = count[right]
            if rightCount == 0:
                right-=1
                continue
            if left + right > limit:
                result+= rightCount
                right-=1
            else:
                if leftCount > rightCount:
                    result += rightCount
                    count[left]-=rightCount
                    count[right]-=rightCount
                    right-=1
                elif leftCount < rightCount:
                    result += leftCount
                    count[left]-=leftCount
                    count[right]-=leftCount
                    left+=1
                else:
                    result += leftCount
                    count[left]-=leftCount
                    count[right]-=leftCount
                    left+=1
                    right-=1
        
        if count[left]!=0:
            peoplePerBoat = min(limit//left,2)
            result += math.ceil(count[left]/peoplePerBoat)
            
        return result
            

