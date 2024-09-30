from lc import *

# https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/539716/JavaC%2B%2BPython-Lazy-increment-O(1)


class CustomStack:
    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val

# https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/539704/JavaPython-3-simple-codes-using-ArrayListlist.

class CustomStack(list):
    def __init__(s, m: int):
        s.s = m
    def push(s, x):
        len(s)<s.s and s.append(x)
    def pop(s):
        return list.pop(s)if s else-1
    def increment(s,k,v):
        for i in range(min(k,len(s))):
            s[i] += v

CustomStack=type('',(list,),{
    '__init__':lambda s,m:setattr(s,'s',m),
    'push':lambda s,x:len(s)<s.s and s.append(x)or None,
    'pop':lambda s:list.pop(s)if s else-1,
    'increment':lambda s,k,v:[setitem(s,i,s[i]+v)for i in range(min(k,len(s)))]and None
})

test('''
1381. Design a Stack With Increment Operation
Medium

1838

99

Add to List

Share
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
 

Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1);                          // stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.push(3);                          // stack becomes [1, 2, 3]
stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100);                // stack becomes [101, 102, 103]
stk.increment(2, 100);                // stack becomes [201, 202, 103]
stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
stk.pop();                            // return -1 --> Stack is empty return -1.
 

Constraints:

1 <= maxSize, x, k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.
Accepted
120,205
Submissions
155,517
''', CustomStack)
