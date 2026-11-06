class TimeMap:

    def __init__(self):
        self.store = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        target = self.store.get(key, [])
        if not target:
            return ""
        res = ""
        
        l = 0
        r = len(target) - 1

        while l <= r:
            mid = (l + r) // 2
            if timestamp >= target[mid][1]:
                res = target[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

