from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        sublist = self.dct[key]
        l, r = 0, len(sublist)-1

        while l <= r:
            m = (l + r) // 2

            if timestamp >= sublist[m][0]:
                val = sublist[m][1]
                l = m + 1
            else:
                r = m - 1

                
        return val or ""

        

                
