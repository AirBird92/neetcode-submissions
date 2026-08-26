class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not pre_map[course]:
                return True
            visited.add(course)
            for prerequisite in pre_map[course]:
                if not dfs(prerequisite):
                    return False
            visited.discard(course)
            pre_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True