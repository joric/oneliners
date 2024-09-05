from lc import *

# https://leetcode.com/problems/count-number-of-teams/discuss/4191569/Python-5-lines.-O(n-log-n)-with-explanation

class Solution:
    def numTeams(self, r: List[int]) -> int:
        a,b=[__import__('sortedcontainers').SortedList(x)for x in(r,[])];return sum((a.remove(v),b.bisect_left(v)*(len(a)-a.bisect_right(v))+(len(b)-b.bisect_right(v))*a.bisect_left(v),b.add(v))[1]for v in r)

# TLE https://leetcode.com/problems/count-number-of-teams/discuss/722827/Python3-Easy-Solution-One-Line

class Solution:
    def numTeams(self, r: List[int]) -> int:
        e=enumerate;return sum(a<b<c or a>b>c for i,a in e(r[:-2])for j,b in e(r[i+1:-1])for c in r[i+j+1:])

# https://leetcode.com/problems/count-number-of-teams/discuss/569865/Python-3-one-line-O(n3)-and-O(n2)

# O(n^3), TLE

class Solution:
    def numTeams(self, r: List[int]) -> int:
        return sum(i<j<k or i>j>k for i,j,k in combinations(r,3))

# O(n^2), O(1) space

class Solution:
    def numTeams(self, r: List[int]) -> int:
        return sum(sum(r[i]<r[j]for j in range(i))*sum(r[i]>r[j]for j in range(i+1,len(r)))+sum(r[i]>r[j]for j in range(i))*sum(r[i]<r[j]for j in range(i+1,len(r)))for i in range(1,len(r)-1))

# O(n^2), O(n) space

class Solution:
    def numTeams(self, r: List[int]) -> int:
        return sum((lambda c:c[0]*c[3]+c[1]*c[2])(Counter((r[i]>r[j])*2+(i>j)for j in range(len(r))if r[i]!=r[j]))for i in range(1,len(r)-1))

test('''
1395. Count Number of Teams
Medium

2644

185

Add to List

Share
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
All the integers in rating are unique.
Accepted
107,735
Submissions
162,922
''')
