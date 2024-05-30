from lc import *

# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/discuss/1232891/Python-3-fast-and-one-line

class Solution:
    def countTriplets(self, a: List[int]) -> int:
        return sum(i*y - (len(I)-i-1)*(y+1) for x,I in reduce(lambda d,x: d[x[1]].append(x[0]) or d, enumerate(accumulate(a, xor, initial=0)), defaultdict(list)).items() for i,y in enumerate(I))        

class Solution:
    def countTriplets(self, a: List[int]) -> int:
        return sum(i*y-(len(j)-i-1)*(y+1)for x,j in reduce(lambda d,x:d[x[1]].append(x[0])or d,enumerate(accumulate(a,xor,initial=0)),defaultdict(list)).items()for i,y in enumerate(j))

class Solution:
    def countTriplets(self, a: List[int]) -> int:
        d = defaultdict(list)
        for i,x in enumerate(accumulate(a,xor,initial=0)):
            d[x].append(i)
        r = 0
        for x,p in d.items():
            r += sum(i*y-(len(p)-i-1)*(y+1)for i,y in enumerate(p))
        return r

class Solution:
    def countTriplets(self, a: List[int]) -> int:
        t,e,d=0,enumerate,defaultdict(list);[d[t:=t^x].append(i)for i,x in e([0]+a)];return sum(i*y+~y*(len(d[x])+~i)for x in d for i,y in e(d[x]))

class Solution:
    def countTriplets(self, a: List[int]) -> int:
        c=Counter;u,v,x=c(),c([0]),0;return sum((u[x:=x^i],u:=u+v,v.update([x]))[0]for i in a)

test('''
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Medium

1366

65

Add to List

Share
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
Accepted
38,384
Submissions
49,796
''')
