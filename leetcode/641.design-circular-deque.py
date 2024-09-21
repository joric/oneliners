from lc import *

# https://leetcode.com/problems/design-circular-deque/discuss/1192441/Python-deque-solution-that-beats-97.7-in-Time-and-86-in-Space

class MyCircularDeque:
    def __init__(self, k: int):
        self.q=deque()
        self.n=k
    def insertFront(self, value: int) -> bool:
        if len(self.q)<self.n:
            self.q.appendleft(value)
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if len(self.q)<self.n:
            self.q.append(value)
            return True
        else:
            return False
    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft()
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            return True
        else:
            return False
    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1
    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        return not self.q
    def isFull(self) -> bool:
        return self.n==len(self.q)

class MyCircularDeque(deque):
    __init__=lambda s,k:setattr(s,'n',k)
    insertFront=lambda s,v:(s.n>len(s)and s.appendleft(v))==None
    insertLast=lambda s,v:(s.n>len(s)and s.append(v))==None
    deleteFront=lambda s:s and(s.popleft(),True)[1]or False
    deleteLast=lambda s:s and(s.pop(),True)[1]or False
    getFront=lambda s:s[0]if s else-1
    getRear=lambda s:s[-1]if s else-1
    isEmpty=lambda s:not s
    isFull=lambda s:s.n==len(s)

MyCircularDeque=type('',(deque,),{
    '__init__':lambda s,k:setattr(s,'n',k),
    'insertFront':lambda s,v:s.n>len(s)and not s.appendleft(v),
    'insertLast':lambda s,v:s.n>len(s)and not s.append(v),
    'deleteFront':lambda s:bool(s and[s.popleft()]),
    'deleteLast':lambda s:bool(s and[s.pop()]),
    'getFront':lambda s:s[0]if s else-1,
    'getRear':lambda s:s[-1]if s else-1,
    'isEmpty':lambda s:not s,
    'isFull':lambda s:s.n==len(s),
})

test('''
641. Design Circular Deque
Medium

1189

77

Add to List

Share
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
 

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
Accepted
76,748
Submissions
133,815
''', classname=MyCircularDeque)
