from lc import *

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/solutions/2421892/python-1-line/?envType=daily-question&envId=2025-05-03

class Solution:
    def minDominoRotations(self, T: List[int], B: List[int]) -> int:
        return -1 if not reduce(lambda r,c:r&(1<<c[0]|1<<c[1]),zip(T,B),0x7e)else len(T)-max(chain(Counter(T).values(), Counter(B).values()))

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/solutions/252242/java-c-python-different-ideas/?envType=daily-question&envId=2025-05-03

class Solution:
    def minDominoRotations(self, A, B):
        for x in [A[0],B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1

class Solution:
    def minDominoRotations(self, A, B):
        s = reduce(set.__and__, (set(d) for d in zip(A, B)))
        if not s: return -1
        x = s.pop()
        return min(len(A) - A.count(x), len(B) - B.count(x))

class Solution:
    def minDominoRotations(self, t: List[int], b: List[int]) -> int:
        return next((len(t)-max(t.count(x),b.count(x))for x in(t[0],b[0])if all(x in d for d in zip(t,b))),-1)

test('''
1007. Minimum Domino Rotations For Equal Row
Solved
Medium
Topics
Companies
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
Seen this question in a real interview before?
1/5
Yes
No
Accepted
234.4K
Submissions
438.9K
Acceptance Rate
53.4%
Topics
Array
Greedy
''')
