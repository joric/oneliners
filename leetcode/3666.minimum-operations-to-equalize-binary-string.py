from lc import *

# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/solutions/7140155/flip-exactly-k-bits-greedy-math-approach-v3c5/

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z = s.count('0')
        n = len(s)
        o = n-z
        if z == 0:
            return 0
        for i in range(1, n + 1):
            p = i * k
            if (p - z) % 2 != 0:
                continue
            if i % 2 == 1:
                if p >= z and p <= (z * i + o * (i - 1)):
                    return i
            else:
                if p >= z and p <= (z * (i - 1) + o * i):
                    return i
        return -1

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z=s.count('0');n=len(s);o=n-z
        if not z: return 0
        for i in range(1,n+1):
            if((p:=i*k)-z)%2<1:
                if z<=p<=z*(t:=(i-1,i))[j:=i%2]+o*t[1-j]:
                    return i
        return -1

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z=s.count('0');n=len(s);o=n-z;return z and next((i for i in range(1,n+1)if((p:=i*k)-z)%2<1 and z<=p<=z*(t:=(i-1,i))[j:=i%2]+o*t[1-j]),-1)or 0

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z=s.count('0');n=len(s);return z and next((i for i in range(1,n+1)if z<=i*k<=n*i-(z,n-z)[i%2]and i*k%2==z%2),-1)or 0

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n=len(s);return(z:=s.count('0'))and next((i for i in range(1,n+1)if z<=i*k<=n*i-(z,n-z)[i%2]and i*k%2==z%2),-1)

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n=len(s);return(z:=s.count('0'))and next((i for i in range(1,n+1)if(z<=i*k<=n*i-(z,n-z)[i%2])*~(i*k^z)%2),-1)

# POTD 2026-02-27

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n,z=len(s),s.count('0');return next((i for i in range(n+1)if(z<=i*k<=n*i-(z,n-z)[i%2])*~(i*k^z)%2),-1)

test('''
3666. Minimum Operations to Equalize Binary String
Hard
Topics
premium lock icon
Companies
Hint
You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

 

Example 1:

Input: s = "110", k = 1

Output: 1

Explanation:

There is one '0' in s.
Since k = 1, we can flip it directly in one operation.
Example 2:

Input: s = "0101", k = 3

Output: 2

Explanation:

One optimal set of operations choosing k = 3 indices in each operation is:

Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".
Thus, the minimum number of operations is 2.

Example 3:

Input: s = "101", k = 2

Output: -1

Explanation:

Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.

Other examples:

Input: s = "0", k = 1
Output: 1

Input: s = "1", k = 1
Output: 0

Input: s = "11", k = 1
Output: 0

Constraints:

1 <= s.length <= 10​​​​​​​5
s[i] is either '0' or '1'.
1 <= k <= s.length
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,200/15.7K
Acceptance Rate
20.4%
Topics
Senior Staff
Math
String
Breadth-First Search
Union-Find
Ordered Set
Biweekly Contest 164
icon
Companies
Hint 1
Model state as z = number of zeros; flipping k picks i zeros (i between max(0, k - (n - z)) and min(k, z)) and transforms z to z' = z + k - 2 * i, so z' lies in a contiguous range and has parity (z + k) % 2.
Hint 2
Build a graph on states 0..n and run BFS from initial z to reach 0; each edge from z goes to all z' in that computed interval.
Hint 3
For speed, keep two ordered sets of unvisited states by parity and erase ranges with lower_bound while BFSing to achieve near O(n log n) time.
''')
