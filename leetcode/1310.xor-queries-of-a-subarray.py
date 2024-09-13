from lc import *

# https://leetcode.com/problems/xor-queries-of-a-subarray/discuss/470787/JavaC%2B%2BPython-Straight-Forward-Solution

class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        for i in range(len(a)-1):
            a[i+1] ^= a[i]
        return [a[j]^a[i-1]if i else a[j]for i,j in q]

# https://leetcode.com/problems/xor-queries-of-a-subarray/discuss/5779356/Solution-by-using-reduce

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        response = []
        cache = {}
        for left, right in queries:
            key = (left, right)
            if key not in cache.keys():
                cache[key] = reduce(lambda x,y: x^y,arr[left:right+1])
            response.append(cache[key])
        return response

class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        f=cache(lambda i,j:reduce(lambda x,y:x^y,a[i:j+1]));return[f(i,j)for i,j in q]

# https://leetcode.com/problems/xor-queries-of-a-subarray/discuss/471231/2-clean-lines-Python

class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        a=[0,*accumulate(a,xor)];return[a[i]^a[j+1]for i,j in q]


test('''
1310. XOR Queries of a Subarray
Medium

1502

37

Add to List

Share
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
 

Constraints:

1 <= arr.length, queries.length <= 3 * 104
1 <= arr[i] <= 109
queries[i].length == 2
0 <= lefti <= righti < arr.length
Accepted
61,244
Submissions
83,566
''')
