from lc import *

# Q2. weekly-contest-377

# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/discuss/4449554/Simple-5-liner-Python-solution.-Find-difference

class Solution:
    def maximizeSquareArea(self, m: int, n: int, h_fences: List[int], v_fences: List[int]) -> int:
        h = sorted(h_fences + [1, m])
        v = sorted(v_fences + [1, n])
        dh = {h[i] - h[j] for i in range(len(h) - 1, 0, -1) for j in range(i)}
        dv = [v[i] - v[j] for i in range(len(v) - 1, 0, -1) for j in range(i)]
        ans = next((x for x in sorted(dv, reverse=True) if x in dh), -1)
        return ans ** 2 % (10**9 + 7) if ans != -1 else -1

# megurine (9th place)

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        a = sorted(a+[1,m])
        b = sorted(b+[1,n])
        s = {abs(x-y) for x,y in combinations(a,2)}
        r = -1
        for x,y in combinations(b,2):
            c = abs(x-y)
            if c in s:
                r = max(c*c,r)
        return r % int(10**9+7) if r>0 else -1

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        a,b=starmap(lambda v,t:{abs(x-y)for x,y in combinations(sorted(v+[1,t]),2)},((a,m),(b,n)));return max(((c*c)%(10**9+7)for c in b if c in a),default=-1)

test('''
2975. Maximum Square Area by Removing Fences From a Field
User Accepted:2702
User Tried:6669
Total Accepted:2832
Total Submissions:23329
Difficulty:Medium
There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

 

Example 1:



Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.
Example 2:



Input: m = 6, n = 7, hFences = [2], vFences = [4]
Output: -1
Explanation: It can be proved that there is no way to create a square field by removing fences.
 

Constraints:

3 <= m, n <= 10^9
1 <= hFences.length, vFences.length <= 600
1 < hFences[i] < m
1 < vFences[i] < n
hFences and vFences are unique.
''')

