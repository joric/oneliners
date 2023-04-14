from lc import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        q = []
        i = 0
        for x in pushed:
            q.append(x)
            while q and q[-1]==popped[i]:
                i += 1
                q.pop()
        return not q

# counters
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        def f(i,j):
            return f(i-1,j+1) if i>=0 and pushed[i]==popped[j] else (i+1,j)
        i = j = 0
        for x in pushed:
            pushed[i] = x
            i,j = f(i,j)
        return i==0

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return reduce(lambda a,x:setitem(pushed,a[0],x) or (f:=(lambda i,j:f(i-1,j+1) if i>=0 and pushed[i]==popped[j] else (i+1,j)))(*a),pushed,(0,0))[0]==0

# pop(0)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        q = [] 
        for x in pushed:
            q.append(x)
            while q and q[-1]==popped[0]:
                q.pop()
                popped.pop(0)
        return not q

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return not reduce(lambda q,x:q.append(x) or next(q for _ in count() if not(q and q[-1]==popped[0] and (q.pop(),popped.pop(0)))),pushed,[])

# recursive

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        def f(a,b,x):
            if not b:
                return 1
            if (i:=a.index(b[0]))==-1 or i<x:
                return 0
            return f(a[:i]+a[i+1:],b[1:],i-1)
        return f(pushed,popped,0)

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return (f:=lambda a,b,x:not b or(i:=a.index(b[0]))>=x and f(a[:i]+a[i+1:],b[1:],i-1))(pushed,popped,0)


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = []
        for x in popped:
            if stack and stack[-1]==x:
                stack.pop()
            else:
                while index<len(pushed):
                    if pushed[index] == x:
                        index += 1
                        break
                    else:
                        stack.append(pushed[index])
                        index += 1
                else:
                    return False
        return True

test('''
946. Validate Stack Sequences
Medium

4040

68

Add to List

Share
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
Accepted
199,431
Submissions
294,658
''')
