from lc import *

# two queues

class MyStack:
    def __init__(self):
        self.a, self.b, self.c = [], [], True
    def push(self, x: int) -> None:
        q,d = (self.a,self.b) if self.c else (self.b,self.a)
        q.append(x)
        while d:
            q.append(d.pop(0))
        self.c = not self.c
    def pop(self) -> int:
        return self.b.pop(0) if self.c else self.a.pop(0)
    def top(self) -> int:
        return self.b[0] if self.c else self.a[0]
    def empty(self) -> bool:
        return not self.b if self.c else not self.a

# one queue

class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return not self.q

# one stack

class MyStack(list):
    def push(s,x):
        s.append(x);
    def top(s):
        return s[-1]
    def empty(s):
        return not s

MyStack=type('',(list,),{'push':list.append,'top':lambda s:s[-1],'empty':lambda s:not s})

test('''
225. Implement Stack using Queues
Easy

5068

1070

Add to List

Share
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack using only one queue?
''',classname=MyStack)

