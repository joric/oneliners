from lc import *

class SmallestInfiniteSet:
    def __init__(self):
        self.deleted = set()
    def popSmallest(self) -> int:
        i = 1
        while i in self.deleted:
            i += 1
        self.deleted.add(i)
        return i
    def addBack(self, num: int) -> None:
        if num in self.deleted:
            self.deleted.remove(num)

SmallestInfiniteSet = type('',(),{'__init__':lambda s:setattr(s,'d',set()),'popSmallest':lambda s:next((s.d.add(i) or i for _ in count() if not(i in s.d and (i:=i+1))),i:=1),'addBack':lambda s,n:n in s.d and s.d.remove(n) or None})

class SmallestInfiniteSet:
    def __init__(self):
        self.r = [*range(1,1001)]
    def popSmallest(self):
        return heappop(self.r)
    def addBack(self, num):
        if num not in self.r:
            heappush(self.r, num)

SmallestInfiniteSet = type('',(),{'__init__':lambda s:setattr(s,'r',[*range(1,1001)]),'popSmallest':lambda s:heappop(s.r),'addBack':lambda s,n:n not in s.r and heappush(s.r,n) or None})

test('''
2336. Smallest Number in Infinite Set
Medium

384

34

Add to List

Share
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

Constraints:

1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
Accepted
29,101
Submissions
40,827
Seen this question in a real interview before?

Yes

No
Based on the constraints, what is the maximum element that can possibly be popped?
Maintain whether elements are in or not in the set. How many elements do we consider?
''',classname=SmallestInfiniteSet)

