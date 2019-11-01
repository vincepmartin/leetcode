from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # It is going to be way easier to work with a dict.
        gDict = {}

        # Put all student grades into the dict.
        for item in items:
            if item[0] in gDict:
                gDict[item[0]].append(item[1])
            else:
                gDict[item[0]] = [item[1]]

        # Return everyones top 5 grades.
        rList = [] 
        for student in gDict:
            rList.append([student, int(sum(sorted(gDict[student], reverse=True)[:5])/5)])

        return rList

s = Solution()
print(s.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))