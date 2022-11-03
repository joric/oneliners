from lc import *

class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, s: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(s)
        for i in range(len(s)):
            for t in range(i + 1)[::-1]:
                if dp[t] >= s[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1

class Solution2:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        def refuel(r, f, h):
            return (-1, 0) if r < 0 else refuel(r + 1, f - heappop(h), h) if f < 0 and h else (r, f) if f >= 0 else (-1, 0)
        def f(a, x):
            result, fuel_left = a
            delta, station_fuel = x
            result, fuel_left = refuel(result, fuel_left - delta, heap)
            return (result, fuel_left*(not heappush(heap, -station_fuel)))
        heap = []
        stations = [[0, startFuel]] + stations + [[target, 0]]
        deltas = [(b[0] - a[0], b[1]) for a, b in zip(stations, stations[1:])]
        return reduce(f, deltas, (0, startFuel))[0]

class Solution3:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        return (
            heap := [],
            s := [[0, startFuel]] + stations + [[target, 0]],
            deltas := [(b[0] - a[0], b[1]) for a, b in zip(s, s[1:])],
            refuel := lambda r, f: (-1, 0) if r < 0 else refuel(r + 1, f - heappop(heap)) if f < 0 and heap else (r, f) if f >= 0 else (-1, 0),
            reduce(lambda a, x: ((t:=refuel(a[0], a[1] - x[0]))[0], t[1]*(not heappush(heap, -x[1]))), deltas, (0, startFuel))[0]
        )[-1]

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        return (heap:=[],s:=[[0,startFuel]]+stations+[[target,0]],deltas:=[(b[0]-a[0],b[1]) for a,b in zip(s,s[1:])],
            refuel:=lambda r,f:(-1,0) if r<0 else refuel(r+1,f-heappop(heap)) if f<0 and heap else (r,f) if f>=0 else(-1,0),
            reduce(lambda a,x:((t:=refuel(a[0],a[1]-x[0]))[0],t[1]*(not heappush(heap,-x[1]))),deltas,(0,startFuel))[0])[-1]


test('''

871. Minimum Number of Refueling Stops
Hard

4127

76

Add to List

Share
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Constraints:

1 <= target, startFuel <= 10^9
0 <= stations.length <= 500
1 <= positioni < positioni+1 < target
1 <= fueli < 10^9
''')
