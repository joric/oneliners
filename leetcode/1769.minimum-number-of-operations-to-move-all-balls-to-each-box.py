from lc import *

# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/solutions/1170285/python-3-true-one-liner/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        A = list(map(int, boxes))
        B = list(accumulate(A))
        return list(accumulate(B[:-1], lambda z,x: z + 2*x - B[-1], initial=sum(starmap(mul, enumerate(A)))))

class Solution: minOperations = lambda _,S: \
    list(accumulate((B := list(accumulate(A := list(map(int, S)))))[:-1], lambda z,x: z + 2*x - B[-1], initial=sum(starmap(mul, enumerate(A)))))

class Solution:
    def minOperations(self, b: str) -> List[int]:
        return[*accumulate((a:=[*accumulate(b:=[*map(int,b)])])[:-1],lambda z,x:z+2*x-a[-1],initial=sum(starmap(mul,enumerate(b))))]

class Solution:
    def minOperations(self, b: str) -> List[int]:
        r=range(len(b));return[sum(abs(j-i)for j in r if'0'<b[j])for i in r]

class Solution:
    def minOperations(self, b: str) -> List[int]:
        r=range(len(b));return[sum(abs(j-i)*int(b[j])for j in r)for i in r]

test('''
1769. Minimum Number of Operations to Move All Balls to Each Box
Solved
Medium
Topics
Companies
Hint
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

 

Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]
 

Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.
''')
