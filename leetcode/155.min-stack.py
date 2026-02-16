from lc import *

# https://leetcode.com/problems/min-stack

# TODO

class MinStack:
    def __init__(self) -> None:
        self.q = []
    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));
    def pop(self) -> None:
        self.q.pop()
    def top(self) -> int:
        return None if len(self.q) == 0 else self.q[len(self.q)-1][0]
    def getMin(self) -> int:
        return None if len(self.q) == 0 else self.q[len(self.q)-1][1]

test('''
155. Min Stack
Solved
Medium
Topics
premium lock icon
Companies
Hint
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,599,019/4.5M
Acceptance Rate
57.7%
Topics
Stack
Design
icon
Companies
Hint 1
Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)
Similar Questions
Sliding Window Maximum
Hard
Max Stack
Hard
''', MinStack)
