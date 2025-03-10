from lc import *

class Solution:
    def mergeArrays(self, a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        return sorted([[k,sum(v for x,v in a+b if x==k)]for k in{x for x,_ in a+b}])

# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/solutions/6483556/two-pointers-one-line/?envType=daily-question&envId=2

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans, p1, p2, n, m = [], 0, 0, len(nums1), len(nums2)
        while p1 < n and p2 < m:   
            if nums1[p1][0] < nums2[p2][0]:
                ans.append(nums1[p1])
                p1 += 1
            elif nums1[p1][0] > nums2[p2][0]:
                ans.append(nums2[p2])
                p2 += 1
            else:
                ans.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
        ans.extend(nums1[p1:])
        ans.extend(nums2[p2:])
        return ans

class Solution:
    def mergeArrays(self, a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        c = Counter()
        for k,v in a+b:
            c[k] += v
        return sorted(c.items())

class Solution:
    def mergeArrays(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        return sorted(add(*map(Counter,(dict(a),dict(b)))).items())

class Solution:
    def mergeArrays(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        return sorted((Counter(dict(a))+Counter(dict(b))).items())

class Solution:
    def mergeArrays(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        return sorted(add(*map(Counter,map(dict,(a,b)))).items())

class Solution:
    def mergeArrays(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c,d=Counter,dict;return sorted((c(d(a))+c(d(b))).items())

class Solution:
    def mergeArrays(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c=Counter;return sorted((c(dict(a))+c(dict(b))).items())

test('''
2570. Merge Two 2D Arrays by Summing Values
Easy
Topics
Companies
Hint
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

 

Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
Example 2:

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
 

Constraints:

1 <= nums1.length, nums2.length <= 200
nums1[i].length == nums2[j].length == 2
1 <= idi, vali <= 1000
Both arrays contain unique ids.
Both arrays are in strictly ascending order by id.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
50.8K
Submissions
68.2K
Acceptance Rate
74.6%
Topics
Array
Hash Table
Two Pointers
Companies
Hint 1
Use a dictionary/hash map to keep track of the indices and their sum values.
Similar Questions
Merge Two Sorted Lists
Easy
Meeting Scheduler
Medium
Merge Similar Items
Easy
''')
