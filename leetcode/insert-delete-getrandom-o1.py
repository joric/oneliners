from lc import *

# https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/1567439/python%3A-using-random-choice

class RandomizedSet:
    def __init__(s):
        s.h = set()
    def insert(s, x: int) -> bool:
        if x in s.h:
            return False
        s.h.add(x)
        return True
    def remove(s, x: int) -> bool:
        if x in s.h:
            s.h.remove(x)
            return True
        return False
    def getRandom(s) -> int:
        return choice([*s.h])

class RandomizedSet:
    def __init__(s):
        s.h = set()
    def insert(s, x: int) -> bool:
        return not(x in s.h or s.h.add(x))
    def remove(s, x: int) -> bool:
        return x in s.h and not s.h.remove(x)
    def getRandom(s) -> int:
        return choice([*s.h])

RandomizedSet=type('',(),{
    '__init__':lambda s:setattr(s,'h',set()),
    'insert':lambda s,x:not(x in s.h or s.h.add(x)),
    'remove':lambda s,x:x in s.h and not s.h.remove(x),
    'getRandom':lambda s:choice([*s.h])
})

RandomizedSet=type('',(),{'__init__':lambda s:setattr(s,'h',set()),'insert':lambda s,x:not(x in s.h or s.h.add(x)),'remove':lambda s,x:x in s.h and not s.h.remove(x),'getRandom':lambda s:choice([*s.h])})

RandomizedSet=type('',(set,),{'insert':lambda s,x:not(x in s or s.add(x)),'remove':lambda s,x:x in s and not s.discard(x),'getRandom':lambda s:choice([*s])})

с=Counter;с.getRandom=lambda s:choice([*s]);с.insert=lambda s,a:s.update([a])or s[a]<2;с.remove=lambda s,a:s.pop(a,0);RandomizedSet=с

test('''
380. Insert Delete GetRandom O(1)
Medium

8352

497

Add to List

Share
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-2^31 <= val <= 2^31 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
Accepted
738,368
Submissions
1,395,843
''', classname=RandomizedSet,check=lambda r,e,*a:setitem(r,4,e[4])or r==e)

