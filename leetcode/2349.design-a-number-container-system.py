from lc import *

# https://leetcode.com/problems/design-a-number-container-system/solutions/2322461/python-solution-using-sortedlist/?envType=daily-question&envId=2025-02-08

from sortedcontainers import SortedList
class NumberContainers:
    def __init__(self):
        self.q = defaultdict(SortedList)
        self.d = {}

    def change(self, i: int, x: int) -> None:
        i in self.d and self.q[self.d[i]].remove(i)
        self.q[x].add(i)
        self.d[i] = x

    def find(self, x: int) -> int:
        return self.q[x][0] if self.q[x] else -1


# https://leetcode.com/problems/design-a-number-container-system/solutions/4700875/two-map-with-heap-no-sortedlist-faster-than-95/?envType=daily-question&envId=2025-02-08

class NumberContainers:
    def __init__(self):
        self.q = defaultdict(list)
        self.d = {}

    def change(self, i: int, x: int) -> None:
        heappush(self.q[x],i)
        self.d[i]=x

    def find(self, x: int) -> int:
        h=self.q[x]
        while h:
            i = heappop(h)
            if self.d[i]==x:
                heappush(h,i)
                return i
        return -1

NumberContainers=type('',(),{
    '__init__':lambda s:setattr(s,'q',defaultdict(list))or setattr(s,'d',{}),
    'change':lambda s,i,x:heappush(s.q[x],i)or setitem(s.d,i,x),
    'find':lambda s,x:(f:=lambda h:(heappush(h,i)or i if x==s.d[i:=heappop(h)]else f(h))if h else-1)(s.q[x])
})

test('''
2349. Design a Number Container System
Medium
Topics
Companies
Hint
Design a number container system that can do the following:

Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:

NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
 

Example 1:

Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]

Explanation
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
 

Constraints:

1 <= index, number <= 109
At most 105 calls will be made in total to change and find.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
25.4K
Submissions
56.3K
Acceptance Rate
45.0%
Topics
Hash Table
Design
Heap (Priority Queue)
Ordered Set
Companies
Hint 1
Use a hash table to efficiently map each number to all of its indices in the container and to map each index to their current number.
Hint 2
In addition, you can use ordered set to store all of the indices for each number to solve the find method. Do not forget to update the ordered set according to the change method.
Similar Questions
Seat Reservation Manager
Medium
Design a Food Rating System
Medium
''', classname=NumberContainers)
