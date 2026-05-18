class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [((target - position[i]) / speed[i]) for i in range(len(position))]
        cars = list(sorted(zip(position, time)))
        fleets = []

        for i in range(len(cars)-1, -1, -1):
            if not fleets or cars[i][1] > fleets[-1]:
                fleets.append(cars[i][1])
            
        return len(fleets)

