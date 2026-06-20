from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.map_ = defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map_[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map_:
            return ""
        
        timestamps = self.map_[key]
        idx = timestamps.bisect_right(timestamp) - 1 # bisect_right - rightmost insertion point

        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return ""
