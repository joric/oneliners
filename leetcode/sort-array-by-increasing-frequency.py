from lc import *

# https://leetcode.com/problems/sort-array-by-increasing-frequency

class Solution:
    def frequencySort(self, n: List[int]) -> List[int]:
        c=Counter(n);return sorted(n,key=cmp_to_key(lambda x,y:c[x]-c[y]or y-x))

class Solution:
    def frequencySort(self, n: List[int]) -> List[int]:
        c=Counter(n);return sorted(n,key=lambda x:(c[x],-x))

# https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/5521428/One-Line-Solution

class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        return sorted(sorted(a)[::-1],key=a.count)

class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        return sorted(a,key=lambda v:(a.count(v),-v))

class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        return sorted(a,key=lambda v,c=Counter(a):(c[v],-v))


class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        return Counter(dict(sorted(Counter(a).items(),key=lambda p:(p[1],-p[0])))).elements()

class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        return chain(*starmap(repeat,sorted(Counter(a).items(),key=lambda p:(p[1],-p[0]))))


class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        return Counter(dict(sorted(Counter(a).items(),key=lambda p:(p[1],-p[0])))).elements()

# https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/5519815/One-line

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return reduce(lambda a,b:a+[b[0]]*b[1],sorted(Counter(nums).items(),key=lambda x:(x[1]<<10)-x[0]),[])

# https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/5519700/One-line

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return [x for x, c in sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0])) for _ in range(c)]

# https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/983217/One-Line-Solution!!!

class Solution:
    def frequencySort(self, n: List[int]) -> List[int]:
        return sorted(sorted(n)[::-1],key=n.count)

test('''
1636. Sort Array by Increasing Frequency
Easy

3116

132

Add to List

Share
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
Accepted
188,801
Submissions
246,653
''')
