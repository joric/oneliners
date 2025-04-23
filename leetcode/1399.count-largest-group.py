from lc import *

# https://leetcode.com/problems/count-largest-group

class Solution:
    def countLargestGroup(self, n: int) -> int:
        return(c:=[*Counter(sum(map(int,str(i+1)))for i in range(n)).values()]).count(max(c))

# https://leetcode.com/problems/count-largest-group/solutions/563356/1-line-python/?envType=daily-question&envId=2025-04-23

class Solution:
    def countLargestGroup(self, n: int) -> int:
        return len(multimode(map(sum,map(map,int,map(str,range(1,n+1))))))

class Solution:
    def countLargestGroup(self, n: int) -> int:
        return len(multimode(sum(map(int,str(i)))for i in range(1,n+1)))

class Solution:
    def countLargestGroup(self, n: int) -> int:
        return len(multimode(sum(map(int,str(i+1)))for i in range(n)))

test('''
1399. Count Largest Group
Solved
Easy
Topics
Companies
Hint
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
Seen this question in a real interview before?
1/5
Yes
No
Accepted
97.8K
Submissions
135.2K
Acceptance Rate
72.4%
Topics
Hash Table
Math
Companies
Hint 1
Count the digit sum for each integer in the range and find out the largest groups.
''')
