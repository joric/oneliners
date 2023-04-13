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
