from lc import *


# https://leetcode.com/problems/valid-triangle-number/solutions/465636/python-2-lines-with-explanations/?envType=daily-question&envId=2025-09-26

class Solution:
    def triangleNumber(self, a: List[int]) -> int:
        d=Counter(a);d=+d;return sum(sum((n-1)*(n-2)//2 for n in range(3,i+1)) for i in d.values())+sum((d[a]-1)*d[a]//2*d[b]for a,b in permutations(d,2) if d[a]>1 and a*2>b)+sum(d[a]*d[b]*d[c]for a,b,c in combinations(d,3) if a+b>c and b+c>a and c+a>b)

# https://leetcode.com/problems/valid-triangle-number/solutions/4370919/8-lines-using-bisect/?envType=daily-question&envId=2025-09-26

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            j = i + 1
            while j < len(nums) - 1:
                res += bisect.bisect_left(nums[j+1:],nums[i] + nums[j])
                j += 1
        return res

class Solution:
    def triangleNumber(self, a: List[int]) -> int:
        a.sort();return sum((j:=i)or sum((j:=j+1)<len(a)and bisect_left(a[j+1:],a[i]+a[j])for _ in a)for i in range(len(a)-2))

class Solution:
    def triangleNumber(self, a: List[int]) -> int:
        a.sort();n=len(a);return sum(sum(bisect_left(a[j+1:],a[i]+a[j])for j in range(i+1,n-1))for i in range(n-2))

class Solution:
    def triangleNumber(self, a: List[int]) -> int:
        a.sort();n=len(a);return sum(sum(bisect_left(a[j+1:],a[i]+a[j])for j in range(i+1,n-1))for i in range(n-2))

test('''
611. Valid Triangle Number
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
239,759/453.9K
Acceptance Rate
52.8%
Topics
Array
Two Pointers
Binary Search
Greedy
Sorting
icon
Companies
Similar Questions
3Sum Smaller
Medium
Find Polygon With the Largest Perimeter
Medium
''')
