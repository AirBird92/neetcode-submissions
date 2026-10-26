class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_list = self.data[key]
        if not value_list:
            return ""
        if timestamp >= value_list[-1][1]:
            return value_list[-1][0]
        if timestamp < value_list[0][1]:
            return ""
        
        l, r = 0, len(value_list)
        res = ""
        while l <= r:
            mid = l + (r - l) // 2
            if timestamp >= value_list[mid][1]:
                res = value_list[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res