class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals

        intervals.sort()
        res = []
        i, j = 0, 1
        while j < n:
            if intervals[i][1] < intervals[j][0]:
                res.append(intervals[i])
                i += 1
                j += 1
            cur_end = intervals[i][1]
            while j < n and cur_end >= intervals[j][0]:
                cur_end = max(cur_end, intervals[j][1])
                j += 1
            res.append([intervals[i][0], cur_end])
            i, j = j, j + 1
        if i == n - 1:
            res.append(intervals[i])
        return res
            