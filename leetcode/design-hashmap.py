from lc import *

class MyHashMap:
    def __init__(self): self.map = [None]*10000000
    def put(self, key: int, value: int) -> None: self.map[key] = value            
    def get(self, key: int) -> int: return self.map[key] if self.map[key]!=None else -1
    def remove(self, key: int) -> None: self.map[key] = None

class MyHashMap(dict): 
    def put(s,k,v):
        setitem(s,k,v)
    def get(s,k):
        return dict.get(s,k,-1)
    def remove(s,k):
        s.pop(k,0)

MyHashMap=type('',(dict,),{'put':dict.__setitem__,'get':lambda s,k:dict.get(s,k,-1),'remove':lambda s,k:s.pop(k,None)and None})

test('''
706. Design HashMap
Easy

4374

388

Add to List

Share
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Example 2:

Input
["MyHashMap","remove","get","put","put","put","get","put","put","put","put"]
[[],[14],[4],[7,3],[11,1],[12,1],[7],[1,19],[0,3],[1,8],[2,6]]
Output [null,null,-1,null,null,null,3,null,null,null,null]

Constraints:

0 <= key, value <= 10^6
At most 104 calls will be made to put, get, and remove.
''', classname=MyHashMap)

