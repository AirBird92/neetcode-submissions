class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        valueList = self.timeMap[key]
        if not valueList:
            return ""
        if timestamp >= valueList[-1][1]:
            return valueList[-1][0]
        if timestamp < valueList[0][1]:
            return ""
        left, right = 0, len(valueList) - 1
        res = ""
        while left <= right:
            mid = left + (right - left) // 2
            if timestamp >= valueList[mid][1]:
                res = valueList[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res