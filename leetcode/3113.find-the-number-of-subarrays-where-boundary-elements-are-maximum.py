from lc import *

# Q4. https://leetcode.com/contest/biweekly-contest-128/
# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

class Solution:
    def numberOfSubarrays(self, a: List[int]) -> int:
        s,r=[],0
        for x in a:
            while s and s[-1][0]<x:
                s.pop()
            if s and s[-1][0] == x:
                s[-1][1] += 1
                r += s[-1][1]
            else:
                s.append([x,1])
                r += 1
        return r

class Solution:
    def numberOfSubarrays(self, a: List[int]) -> int:
        s,r=[],0;[(all(s and s[-1][0]<x and[s.pop()]for _ in a),s and(t:=s[-1])[0]==x and(setitem(t,1,t[1]+1),r:=r+t[1])or(s.append([x,1]),r:=r+1))for x in a];return r

# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/discuss/5017752/Simple-5-line-python-code.

class Solution:
    def numberOfSubarrays(self, a: List[int]) -> int:
        s,c,r=[],Counter(),0
        for i,x in enumerate(a):
            while s and s[-1]<x:
                c[s.pop()] -= 1
            s.append(x)
            c[x] += 1
            r += c[x]
        return r

class Solution:
    def numberOfSubarrays(self, a: List[int]) -> int:
        s,c=[],Counter();return sum((all(s and x>s[-1]and[c.update({s.pop():-1})]for _ in a),s.append(x),c.update([x]),c[x])[3]for i,x in enumerate(a))

test('''
3113. Find the Number of Subarrays Where Boundary Elements Are Maximum
Hard

21

3

Add to List

Share
You are given an array of positive integers nums.

Return the number of subarrays of nums, where the first and the last elements of the subarray are equal to the largest element in the subarray.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 6

Explanation:

There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

subarray [1,4,3,3,2], with its largest element 1. The first element is 1 and the last element is also 1.
subarray [1,4,3,3,2], with its largest element 4. The first element is 4 and the last element is also 4.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 2. The first element is 2 and the last element is also 2.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
Hence, we return 6.

Example 2:

Input: nums = [3,3,3]

Output: 6

Explanation:

There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
Hence, we return 6.

Example 3:

Input: nums = [1]

Output: 1

Explanation:

There is a single subarray of nums which is [1], with its largest element 1. The first element is 1 and the last element is also 1.

Hence, we return 1.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
Accepted
2,578
Submissions
18,021
''')