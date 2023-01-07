from lc import *

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        max_so_far = 0
        max_ending_here = 0
        dist = 0

        for i in range(n*2):
            max_ending_here += gas[i % n] - cost[i % n]
            if max_ending_here < 0:
                max_ending_here = 0
                max_so_far = (i + 1) % n
                dist = 0
            else:
                dist +=1
                if dist == n:
                    break
                
        return -1 if dist < n else max_so_far


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t = b = 0
        for i in range(len(gas)):
            t += gas[i] - cost[i]
            if  t < 0:
                t = 0
                b = i + 1
        return -1 if sum(gas) < sum(cost) else b


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return -1 if sum(gas)<sum(cost) else reduce(lambda p,i:p.__setitem__(0, p[0]+gas[i]-cost[i]) or ([0,i+1] if p[0]<0 else p), range(len(gas)),(0,0))[1]


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return -1 if sum(gas)<sum(cost) else reduce(lambda p,d:(0,p[2]+1,p[2]+1) if p[0]+d<0 else (p[0]+d,p[1],p[2]+1),map(sub,gas,cost),(0,0,0))[1]


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return -1 if sum(gas)<sum(cost) else (t:=0,b:=0) and [(t:=t+gas[i]-cost[i],t<0)[1] and (t:=0,b:=i+1) for i in range(len(gas))] and b


test('''

134. Gas Station
Medium

7629

707

Add to List

Share
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


Example 3:

Input: gas = [5,1,2,3,4], cost = [4,4,1,5,1]
Output: 4

Constraints:

n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4

''')
