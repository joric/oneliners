from lc import *

# https://leetcode.com/problems/sorted-gcd-pair-queries/solutions/5878001/python3-13-lines-by-nguyenquocthao00-la2b/?envType=daily-question&envId=2026-07-17

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxv=max(nums)
        co,lcount = [0]*(maxv+1), [0]*(maxv+1)
        for v in nums: co[v]+=1
        for i in range(1, maxv+1):
            x = 0
            for mul in range(i, maxv+1, i): x+=co[mul]
            lcount[i]=x*(x-1)//2
        for i in range(maxv, 0, -1):
            for mul in range(2*i, maxv+1, i): lcount[i] -= lcount[mul]
        acc=list(accumulate(lcount))
        return [bisect.bisect_right(acc, q) for q in queries]

class Solution:
    def gcdValues(self, n: List[int], q: List[int]) -> List[int]:
        m=max(n)+1;c=Counter(n);l=[0]*m;r=range;[setitem(l,i,(x:=sum(c[j]for j in r(i,m,i)))*(x-1)//2-sum(l[j]for j in r(2*i,m,i)))for i in r(m-1,0,-1)];a=[*accumulate(l)];return[bisect_right(a,v)for v in q]


class Solution:
    def gcdValues(self, n: List[int], q: List[int]) -> List[int]:
        m=max(n);c=Counter(n);l=[0]*(m+1);[setitem(l,i,comb(sum(c[j]for j in range(i,m+1,i)),2)-sum(l[2*i::i]))for i in range(m,0,-1)];a=[*accumulate(l)];return[bisect_right(a,v)for v in q]

test('''
3312. Sorted GCD Pair Queries
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.

 

Example 1:

Input: nums = [2,3,4], queries = [0,2,2]

Output: [1,2,2]

Explanation:

gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].

After sorting in ascending order, gcdPairs = [1, 1, 2].

So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].

Example 2:

Input: nums = [4,4,2,1], queries = [5,3,1,0]

Output: [4,2,1,1]

Explanation:

gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].

Example 3:

Input: nums = [2,2], queries = [0,0]

Output: [2,2]

Explanation:

gcdPairs = [2].

 

Constraints:

2 <= n == nums.length <= 105
1 <= nums[i] <= 5 * 104
1 <= queries.length <= 105
0 <= queries[i] < n * (n - 1) / 2
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
6,361/27K
Acceptance Rate
23.6%
Topics
Principal
Array
Hash Table
Math
Binary Search
Combinatorics
Counting
Number Theory
Prefix Sum
Weekly Contest 418
icon
Companies
Hint 1
Try counting the number of pairs that have a GCD of g
Hint 2
Use inclusion-exclusion.
''')
