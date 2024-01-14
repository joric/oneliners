from lc import *

def init(n, bad):
    global p
    p = bad

def isBadVersion(n):
    global p
    return n>=p

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return bisect_left(range(n+1),1,key=isBadVersion)

test('''
278. First Bad Version
Easy

8196

3242

Add to List

Share
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4

Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 2^31 - 1
Accepted
1,611,784
Submissions
3,659,054
''', init=init)

