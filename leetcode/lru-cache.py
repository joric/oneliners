from lc import *

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = dict()

    def get(self, key: int) -> int:
        if key in self.items:
            item = self.items[key]
            del self.items[key]
            self.items[key] = item
            return item
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            del self.items[key]
        if len(self.items) == self.capacity:
            k = next(iter(self.items.keys()))
            del self.items[k]
        self.items[key] = value


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        val = self.dic[key]
        self.dic.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)


LRUCache=type('',(),{
    '__init__':lambda s,c:setattr(s,'c',c)or setattr(s,'d',OrderedDict()),
    'get':lambda s,k:s.d.move_to_end(k)or s.d[k]if k in s.d else-1,
    'put':lambda s,k,v:(setitem(s.d,k,v),s.d.move_to_end(k),len(s.d)>s.c and s.d.popitem(0))
})


LRUCache=type('',(),{'__init__':lambda s,c:setattr(s,'c',c)or setattr(s,'d',OrderedDict()),'get':lambda s,k:s.d.move_to_end(k)or s.d[k]if k in s.d else-1,'put':lambda s,k,v:(setitem(s.d,k,v),s.d.move_to_end(k),len(s.d)>s.c and s.d.popitem(0))})

test('''
146. LRU Cache
Medium

15597

654

Add to List

Share
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

''', LRUCache, check=lambda res,exp,*met:all(1 if m=='put' else r==e for r,e,m in zip(res,exp,met)))
