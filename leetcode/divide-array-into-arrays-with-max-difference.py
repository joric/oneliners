from lc import *

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        n.sort()
        r = []
        for i in range(0,len(n),3):
            if k<n[i+2]-n[i]:
                return []
            r.append(n[i:i+3])
        return r

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        n.sort();r=[];return next(([]for i in range(0,len(n),3)if k<n[i+2]-n[i]or r.append(n[i:i+3])),r)

# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/discuss/4656961/One-line-solution.-Runtime-greater-99

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        r = []
        for n in zip(*[iter(sorted(n))]*3):
            if n[2]-n[0]<=k:
                r.append(n)
            else:
                return []
        return r

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        return(r:=[*takewhile(lambda n:n[2]-n[0]<=k,zip(*[iter(sorted(n))]*3))])*(len(r)*3==len(n))

# updated 1 Feb 2024

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        r=*zip(*[iter(sorted(n))]*3),;return all(k>=b-a for a,_,b in r)and r or[]

# python 3.12 for the better leetcode in the future (-5 chars)
class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        r=*batched(sorted(n),3),;return all(k>=b-a for a,_,b in r)and r or[]

test(''''
2966. Divide Array Into Arrays With Max Difference
Medium

200

48

Add to List

Share
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

 

Example 1:

Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.
Example 2:

Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
 

Constraints:

n == nums.length
1 <= n <= 105
n is a multiple of 3.
1 <= nums[i] <= 105
1 <= k <= 105
Accepted
37,365
Submissions
58,517
''')

