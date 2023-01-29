from lc import *


class LFUCache:
    def __init__(self, capacity: int):
        self.f = defaultdict(OrderedDict)
        self.k = {}
        self.c = capacity

    def get(self, key: int) -> int:
        if key not in self.k:
            return -1
        f = self.k[key]
        x = self.f[f].pop(key)
        self.k[key] = f+1
        if not self.f[f]:
            del self.f[f]
        self.f[f+1][key] = x
        return x

    def put(self, key: int, value: int) -> None:
        if key in self.k:
            f = self.k[key]
            self.get(key)
            self.f[f+1][key] = value
        elif self.c:
            if len(self.k) == self.c:
                l = min(self.f)
                p = self.f[l].popitem(last = False)[0]
                del self.k[p]
                if not self.f[l]:
                    del self.f[l]
            self.f[1][key] = value
            self.k[key] = 1


class LFUCache:
    def __init__(s,c):
        setattr(s,'f',defaultdict(OrderedDict)) or setattr(s,'k',{}) or setattr(s,'c',c)
    def get(s,k):
        return -1 if k not in s.k else (f:=s.k[k],x:=s.f[f].pop(k),setitem(s.k,k,f+1),not s.f[f] and s.f.pop(f),setitem(s.f[f+1],k,x)) and x
    def put(s,k,v):
        (f:=s.k[k],s.get(k),setitem(s.f[f+1],k,v)) if k in s.k else s.c and (len(s.k)==s.c and (l:=min(s.f),
        p:=s.f[l].popitem(last=0)[0],s.k.pop(p),not s.f[l] and s.f.pop(l)),setitem(s.f[1],k,v),setitem(s.k,k,1))


LFUCache = type('',(),{'__init__':lambda s,c:setattr(s,'f',defaultdict(OrderedDict)) or setattr(s,'k',{}) or setattr(s,'c',c),'get':lambda s,k:-1 if k not in s.k else (f:=s.k[k],x:=s.f[f].pop(k),setitem(s.k,k,f+1),not s.f[f] and s.f.pop(f),setitem(s.f[f+1],k,x)) and x,'put':lambda s,k,v:((f:=s.k[k],s.get(k),setitem(s.f[f+1],k,v)) if k in s.k else s.c and (len(s.k)==s.c and (l:=min(s.f),p:=s.f[l].popitem(last=0)[0],s.k.pop(p),not s.f[l] and s.f.pop(l)),setitem(s.f[1],k,v),setitem(s.k,k,1))) and None})

test('''

460. LFU Cache
Hard

3985

243

Add to List

Share
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.
 

''',LFUCache)
