from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        sublist = self.dct[key]
        for t, v in sublist[::-1]:
            if timestamp >= t: return v
        return ""


                
