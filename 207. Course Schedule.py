"""
Question:
https://leetcode.com/problems/course-schedule/description/
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        num_pres = [0] * numCourses
        course_pre = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            num_pres[course] += 1
            course_pre[pre].append(course)

        learnt = [course for course, num_pre in enumerate(num_pres) if not num_pre]

        while learnt:
            course = learnt.pop(0)
            for pre_req in course_pre[course]:
                num_pres[pre_req] -= 1
                if not num_pres[pre_req]:
                    learnt.append(pre_req)

        return not any(num_pres)
