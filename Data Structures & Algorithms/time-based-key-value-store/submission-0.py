class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[f"{key}-{timestamp}"] = value

    def get(self, key: str, timestamp: int) -> str:
        key_search, timestamp_prev = None, 0
        for k, v in self.dct.items():
            k_key, k_timestamp = k.split("-")
            if key == k_key:
                timestamp_prev = max(int(timestamp_prev), int(k_timestamp))
                key_search = f"{key}-{timestamp_prev}"
        return self.dct[key_search]
                
                
