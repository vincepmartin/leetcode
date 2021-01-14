from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        grades = {}
        topFiveGrades = []

        # Populate the grades dict.       
        for i in items:
            student = i[0]
            grade = i[1]

            if student in grades:
                grades[student].append(grade)
            else:
                grades[student] = [grade]


        # Calculate the top 5 average in grades.
        for student in sorted(grades.keys()):
            grades[student] = sorted(grades[student], reverse=True)
            grades[student] = sum(grades[student][0:5]) // 5
            topFiveGrades.append([student, grades[student]])

        return topFiveGrades

s = Solution()
t1 = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(s.highFive(t1))