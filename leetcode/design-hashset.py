from lc import *

# https://leetcode.com/problems/design-hashset/discuss/768659/Python-Easy-Multiplicative-Hash-explained

class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key):
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key):
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key):
        t = self.eval_hash(key)
        return key in self.arr[t]

class MyHashSet: 
    def __init__(self):
        self.a = set()
    def add(self, key):
        self.a.add(key)
    def remove(self, key):
        self.a.discard(key)
    def contains(self, key):
        return key in self.a

MyHashSet=type('',(),{'__init__':lambda s:setattr(s,'a',set()),'add':lambda s,k:s.a.add(k),'remove':lambda s,k:s.a.discard(k),'contains':lambda s,k:k in s.a})

test('''
705. Design HashSet
Easy

2710

241

Add to List

Share
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 

Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
Accepted
287,197
Submissions
437,969
Seen this question in a real interview before?

Yes

No
Design HashMap
Easy
Design Skiplist
Hard
''',classname=MyHashSet)

