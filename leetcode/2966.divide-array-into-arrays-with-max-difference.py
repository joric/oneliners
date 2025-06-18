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

class Solution:
    def divideArray(self, a: List[int], k: int) -> List[List[int]]:
        a.sort();r=range(0,len(a),3);return[a[i:i+3]for i in r]*all(k>=a[i+2]-a[i]for i in r)

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

# updated 2024-02-01
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/discuss/4656961/One-line-solution.-Runtime-greater-99

class Solution: # python 3.12 ftw / doesn't work on leetcode 2025-06-18 just yet
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        return([],r:=[*batched(sorted(n),3)])[all(k>=b-a for a,_,b in r)]

class Solution:
    def divideArray(self, a: List[int], k: int) -> List[List[int]]:
        return(r:=[*batched(sorted(a),3)])*all(q-p<=k for p,_,q in r)

# POTD 2025-06-18

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        r=[*zip(*[iter(sorted(n))]*3)];return all(a[2]<=a[0]+k for a in r)and r or[]

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        r=*zip(*[iter(sorted(n))]*3),;return([],r)[all(k>=b-a for a,_,b in r)]

class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        return([],r:=[*zip(*[iter(sorted(n))]*3)])[all(k>=b-a for a,_,b in r)]

class Solution:
    def divideArray(self, a: List[int], k: int) -> List[List[int]]:
        return(r:=[*zip(*[iter(sorted(a))]*3)])*all(q-p<=k for p,_,q in r)

class Solution:
    def divideArray(self, a: List[int], k: int) -> List[List[int]]:
        r=*zip(*[iter(sorted(a))]*3),;return r*all(q-p<=k for p,_,q in r)

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
1 <= n <= 10^5
n is a multiple of 3.
1 <= nums[i] <= 10^5
1 <= k <= 10^5
Accepted
37,365
Submissions
58,517
''')
