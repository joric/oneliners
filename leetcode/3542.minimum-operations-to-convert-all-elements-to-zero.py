from lc import *

# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/solutions/7208350/easy-python-solution-by-sb012-dzap/

class Solution:
    def minOperations(self, a: List[int]) -> int:
        r=0;s=[]
        for i in a:
            while s and s[-1]>=i:
                p=s.pop()
                if p!=i:
                    r+=1
            s+=i,
        return r+len({i for i in s if i})

class Solution:
    def minOperations(self, a: List[int]) -> int:
        r,s=0,[]
        for i in a:
            r+=(f:=lambda i:s and i<=s[-1]and(s.pop()!=i)+f(i)or 0)(i)
            s+=i,
        return r+len({*filter(None,s)})

class Solution:
    def minOperations(self, a: List[int]) -> int:
        s=[];return sum(((f:=lambda i:s and i<=s[-1]and(s.pop()!=i)+f(i)or 0)(i),s.append(i))[0]for i in a)+len({*filter(None,s)})

# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/solutions/7331617/five-simple-lines-of-code-by-mikposp-gwrq/?envType=daily-question&envId=2025-11-10

class Solution:
    def minOperations(self, a: List[int]) -> int:
        res,st = 0,[]
        for v in chain(a,[0]):
            while st and st[-1]>=v: res += st.pop()>v
            st.append(v)
        return res

class Solution:
    def minOperations(self, a: List[int]) -> int:
        r,s = 0,[]
        for x in a+[0]:
            while s and s[-1]>=x:r+=x<s.pop()
            s.append(x)
        return r

class Solution: #TLE
    def minOperations(self, a: List[int]) -> int:
        s=[];return sum((sum(x<s.pop()for _ in a if[x]<=s[-1:]),s.append(x))[0]for x in a+[0])

class Solution:
    def minOperations(self, a: List[int]) -> int:
        s=[];return sum((sum(x<s.pop()for _ in iter(lambda:[x]<=s[-1:],0)),s.append(x))[0]for x in a+[0])

class Solution:
    def minOperations(self, a: List[int]) -> int:
        s=[];return sum(((f:=lambda:[x]<=s[-1:]and x<s.pop()and f()+1)(),s.append(x))[0]for x in a+[0])

test('''
3542. Minimum Operations to Convert All Elements to Zero
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0.

 

Example 1:

Input: nums = [0,2]

Output: 1

Explanation:

Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
Thus, the minimum number of operations required is 1.
Example 2:

Input: nums = [3,1,2,1]
Output: 3

Explanation:

Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
Thus, the minimum number of operations required is 3.
Example 3:

Input: nums = [1,2,1,2,1,2]

Output: 4

Explanation:

Select subarray [0,5] (which is [1,2,1,2,1,2]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [0,2,0,2,0,2].
Select subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,2,0,2].
Select subarray [3,3] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,2].
Select subarray [5,5] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,0].
Thus, the minimum number of operations required is 4.

Other examples:

Input: nums = [1,3]
Output: 2

Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,159/43.6K
Acceptance Rate
25.6%
Topics
Array
Hash Table
Stack
Greedy
Monotonic Stack
Biweekly Contest 156
icon
Companies
Hint 1
Process the values in nums from smallest to largest (excluding 0).
Hint 2
For each target value v, identify its maximal contiguous segments (subarrays where nums[i] == v); each segment can be zeroed out in one operation.
Hint 3
After setting those segments to zero, dynamically update the remaining array and repeat with the next value.
''')
