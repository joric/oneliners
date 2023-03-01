from lc import *

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units
                return ans
        return ans

# https://leetcode.com/problems/maximum-units-on-a-truck/discuss/999325/Python-oneliner-(greedy)/807296/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def fn(a,b):
            truckSize, acc = a
            boxes, units = b
            return truckSize - min(truckSize, boxes), acc + min(truckSize, boxes)*units
        return reduce(fn, sorted(boxTypes,key=lambda x:x[1], reverse=True), [truckSize, 0])[1]

class Solution:
    def maximumUnits(self, b: List[List[int]], t: int) -> int:
        return reduce(lambda a,b:(a[0]-min(a[0],b[0]),a[1]+min(a[0],b[0])*b[1]),sorted(b,key=lambda x:x[1])[::-1],[t,0])[1]

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = [[-u, -b] for b, u in boxTypes]
        heapify(heap)
        units = 0
        while heap:
            u, b = heappop(heap)
            if -b > truckSize:
                return units - truckSize * u
            units += u * b
            truckSize += b
        return units

class Solution:
    def maximumUnits(self, b: List[List[int]], t: int) -> int:
        return sum(sorted(u for n, u in b for u in [u] * n)[-t:])

test('''

1710. Maximum Units on a Truck
Easy

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 10**6
''')
