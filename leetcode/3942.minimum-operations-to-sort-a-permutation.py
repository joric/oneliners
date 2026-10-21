from lc import *

# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/solutions/8293610/greedy-simple-7-lines-time-on-space-o1-b-oply/?envType=daily-question&envId=2026-10-22

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums.index(0)
        if all(i == nums[(start + i) % n] for i in range(n)):
            return min(start, n - start + 2) 
        if all(i == nums[(start - i) % n] for i in range(n)):
            return min(start + 2, n - start)
        return -1

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n = len(a)
        j = a.index(0)
        if all(i == a[(j + i) % n] for i in range(n)):
            return min(j, n - j + 2) 
        if all(i == a[(j - i) % n] for i in range(n)):
            return min(j + 2, n - j)
        return -1

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n=len(a);j=a.index(0);r=[*range(n)];return min(j,n-j+2)if r==a[j:]+a[:j]else min(j+2,n-j)if r==a[j::-1]+a[:j:-1]else-1

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n=len(a);j=a.index(0);r=[*range(1,n)];b=a[j+1:]+a[:j];return min(x:=[-1,j,n-j][b==r or(b[::-1]==r)*2],n-x+2)

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n=len(a);q,*b=a;d=sum(map(gt,a,b+a));return(q+d>1)*min(n-q,q+2)|-(1<d<n-1)

test('''
3942. Minimum Operations to Sort a Permutation
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:

Reverse the entire array.
Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

 

Example 1:

Input: nums = [0,2,1]

Output: 2

Explanation:

Rotate Left by one: [2, 1, 0]
Reverse the array: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal

Example 2:

Input: nums = [1,0,2]

Output: 2

Explanation:

Reverse the array: [2, 0, 1]
Rotate Left by one: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal.

Example 3:

Input: nums = [2,0,1,3]

Output: -1

Explanation:

It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.

 

Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= n - 1
nums is a permutation of integers from 0 to n - 1.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
15,983/57.2K
Acceptance Rate
28.0%
Topics
Staff
Array
Weekly Contest 503
icon
Companies
Hint 1
1a. (Case Analysis) The operations generate only rotations of nums and rotations of reverse(nums).
Hint 2
1b. (Case Analysis) So sorting is possible if and only if nums is a rotation of increasing order, or a rotation of decreasing order.
Hint 3
1c. (Case Analysis) If nums is increasing cyclically and nums[i] = 0, then rotating left i times sorts the array, or we may reverse, rotate, then reverse again. Take the minimum between these possibilities.
Hint 4
1d. (Case Analysis) If nums is decreasing cyclically, try both possibilities: reverse first, or rotate first and then reverse. Take the minimum valid cost.
Hint 5
2a. (Breadth-First Search) As follows from Hint 1a and 1b, each reachable array can be represented as a state. Since all reachable arrays belong to one of two families, we can compress a state into (type, shift). type = 0: a rotation of the original array. type = 1: a rotation of the reversed array. shift denotes the number of left rotations applied within that family.
Hint 6
2b. (Breadth-First Search) A left rotation changes shift to (shift + 1) % n. A reverse toggles type, while also changing the corresponding shift to (n - shift) % n.
Hint 7
2c. (Breadth-First Search) Build a graph on these 2n states using the two allowed operations, then run BFS from (0, 0) to the state representing the input array.
''')
