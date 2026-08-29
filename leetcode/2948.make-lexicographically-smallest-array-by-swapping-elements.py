from lc import *

# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/solutions/6328399/five-simple-lines-of-code-by-mikposp-h9mb/?envType=daily-question&envId=2026-08-29

class Solution:
    def lexicographicallySmallestArray(self, a: List[int], l: int) -> List[int]:
        vv,ii = zip(*sorted(zip(a+[inf], count())))
        for i,j in pairwise([0]+[i for i in range(1,len(vv)) if vv[i]-vv[i-1]>l]):
            for k,v in zip(sorted(ii[i:j]), vv[i:j]):
                a[k] = v
        return a

class Solution:
    def lexicographicallySmallestArray(self, a: List[int], b: int) -> List[int]:
        v,i=zip(*sorted(zip(a+[inf],count())));[setitem(a, k,x)for p,q in pairwise([0]+[j for j in range(len(v))if v[j]-v[j-1]>b])for k,x in zip(sorted(i[p:q]),v[p:q])];return a

# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/solutions/6326874/3-lines-of-easy-python3-code-onlogn-by-s-fug3/?envType=daily-question&envId=2026-08-29

class Solution:
    def lexicographicallySmallestArray(self, a: List[int], b: int) -> List[int]:
        q,p=[[inf]],{};[q[-1][-1]-c>b and q.append([])or p.setdefault(c,q[-1]).append(c)for c in sorted(a)[::-1]];return[p[c].pop()for c in a]

class Solution:
    def lexicographicallySmallestArray(self, a: List[int], b: int) -> List[int]:
        g,p=[inf],{};[b+c<g[-1]and(g:=[])or p.setdefault(c,g).append(c)for c in sorted(a)[::-1]];return[p[c].pop()for c in a]

class Solution:
    def lexicographicallySmallestArray(self, a: List[int], b: int) -> List[int]:
        g,p=[-b],{};[c-b>g[-1]and(g:=[])or p.setdefault(c,g).append(c)for c in sorted(a)];return[p[c].pop(0)for c in a]

class Solution:
    def lexicographicallySmallestArray(self, a: List[int], b: int) -> List[int]:
        g=-b,;p={(g:=(g,[])[c-b>g[-1]]).append(c)or c:g for c in sorted(a)};return[p[c].pop(0)for c in a]

test('''
2948. Make Lexicographically Smallest Array by Swapping Elements
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

 

Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.
Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.
Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= limit <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
104,996/173.8K
Acceptance Rate
60.4%
Topics
Staff
Array
Union-Find
Sorting
Weekly Contest 373
icon
Companies
Hint 1
Construct a virtual graph where all elements in nums are nodes and the pairs satisfying the condition have an edge between them.
Hint 2
Instead of constructing all edges, we only care about the connected components.
Hint 3
Can we use DSU?
Hint 4
Sort nums. Now we just need to consider if the consecutive elements have an edge to check if they belong to the same connected component. Hence, all connected components become a list of position-consecutive elements after sorting.
Hint 5
For each index of nums from 0 to nums.length - 1 we can change it to the current minimum value we have in its connected component and remove that value from the connected component.
Similar Questions
Smallest String With Swaps
Medium
Minimize Hamming Distance After Swap Operations
Medium
''')
