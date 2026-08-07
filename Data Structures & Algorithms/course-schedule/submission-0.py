class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for c, p in prerequisites:
            preMap[c].append(p)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not preMap[course]:
                return True
            
            visited.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False
            visited.discard(course)
            preMap[course] = []
            return True
        for c, _ in prerequisites:
            if not dfs(c):
                return False
        return True