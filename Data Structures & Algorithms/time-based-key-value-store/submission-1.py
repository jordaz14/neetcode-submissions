from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        sublist = self.dct[key]
        sublist.sort()
        return sublist[-1][-1]

                
