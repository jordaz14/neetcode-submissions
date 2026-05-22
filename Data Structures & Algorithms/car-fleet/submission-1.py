class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = sorted([(position[i], ((target - position[i]) / speed[i])) for i in range(len(position))])
        fleets = []

        for i in range(len(position)-1, -1, -1):
            if not fleets or time[i][1] > fleets[-1]:
                fleets.append(time[i][1])

        return (len(fleets))