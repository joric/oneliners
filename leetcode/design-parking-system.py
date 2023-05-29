from lc import *

# https://leetcode.com/problems/design-parking-system/discuss/3573371/PythonJavaC%2B%2BSimple-SolutionEasy-to-Understand

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.sports = [big, medium, small]
    def addCar(self, carType: int) -> bool:
        if self.sports[carType-1]>0:
            self.sports[carType-1]-=1
            return True
        else:
            return False

class ParkingSystem:
    def __init__(s, a: int, b: int, c: int):
        s.p = [0,a,b,c]
    def addCar(s, t: int) -> bool:
        return s.p[t]>0 and not setitem(s.p,t,s.p[t]-1)

ParkingSystem=type('',(),{'__init__':lambda s,a,b,c:setattr(s,'p',[0,a,b,c]),'addCar':lambda s,t:s.p[t]>0 and not setitem(s.p,t,s.p[t]-1)})

test('''
1603. Design Parking System
Easy

1308

387

Add to List

Share
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
 

Example 1:

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
 

Constraints:

0 <= big, medium, small <= 1000
carType is 1, 2, or 3
At most 1000 calls will be made to addCar
Accepted
196,835
Submissions
223,193
Seen this question in a real interview before?

Yes

No
Record number of parking slots still available for each car type.
''',classname=ParkingSystem)
