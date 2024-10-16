from lc import *

class MyQueue:
    def __init__(self):
        self.i, self.o = [],[]

    def push(self, x):
        self.i.append(x)

    def pop(self):
        self.peek()
        return self.o.pop()

    def peek(self):
        if not self.o:
            while self.i:
                self.o.append(self.i.pop())
        return self.o[-1]

    def empty(self):
        return not self.i and not self.o

# https://leetcode.com/problems/implement-queue-using-stacks/discuss/2917115/Python-3-one-line

MyQueue = type('MyQueue',(),{
    '__init__':lambda s:setattr(s,'i',[]) or setattr(s,'o',[]),
    'push':lambda s,x:s.i.append(x),
    'pop':lambda s:s.peek() and s.o.pop(),
    'peek':lambda s:(not s.o and next(0 for _ in count() if not (s.i and not s.o.append(s.i.pop())))) or s.o[-1],
    'empty':lambda s:not s.i and not s.o
})

MyQueue=type('MyQueue',(),{'__init__':lambda s:setattr(s,'i',[])or setattr(s,'o',[]),'push':lambda s,x:s.i.append(x),'pop':lambda s:s.peek()and s.o.pop(),'peek':lambda s:(not s.o and next(0 for _ in count()if not(s.i and not s.o.append(s.i.pop()))))or s.o[-1],'empty':lambda s:not s.i and not s.o})

MyQueue=type('',(deque,),{
    'push':lambda s,x:s.append(x),
    'peek':lambda s:s[0],
    'pop':lambda s:s.popleft(),
    'empty':lambda s:not s
})

MyQueue=type('',(deque,),{'push':deque.append,'peek':lambda s:s[0],'pop':deque.popleft,'empty':lambda s:not s})

c=type('',(deque,),{});c.push=c.append;c.peek=lambda s:s[0];c.pop=c.popleft;c.empty=lambda s:not s;MyQueue=c

test('''

232. Implement Queue using Stacks
Easy

4723

303

Add to List

Share
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

''', MyQueue)
