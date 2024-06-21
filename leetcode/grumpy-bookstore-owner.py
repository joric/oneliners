from lc import *

# https://leetcode.com/problems/grumpy-bookstore-owner/discuss/408313/AC-readable-Python-9-lines/2468936

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        u=[o:=0]*2
        for i in range(len(c)):
            u[g[i]]+=c[i]
            u[1]-=(j:=i-m)>=0 and g[j]*c[j]
            o=max(o,u[1])
        return u[0]+o

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        u=[o:=0]*2;[(setitem(u,g[i],u[g[i]]+c[i]),setitem(u,1,u[1]-((j:=i-m)>=0 and g[j]*c[j])),o:=max(o,u[1]))for i in range(len(c))];return u[0]+o

# https://leetcode.com/problems/grumpy-bookstore-owner/discuss/2640151/3-lines-Python

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        p = [0] + list(accumulate(c * (1-g) for c, g in zip(customers, grumpy)))
        acc = [0] + list(accumulate(customers))
        return max(p[-1] - p[i+minutes] + p[i] + acc[i+minutes] - acc[i] for i in range(len(acc) - minutes))

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        a=accumulate;p,q=[0,*a(map(mul,c,map(not_,g)))],[0,*a(c)];return max(p[-1]-p[i+m]+p[i]+q[i+m]-q[i]for i in range(len(q)-m))

# https://leetcode.com/problems/grumpy-bookstore-owner/discuss/5345871/Python-simple-numpy-solution-for-people-who-are-familiar-with-linear-algebra

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        import numpy as np
        c,g = map(np.array,(c,g))
        i = np.argmax(np.convolve(c*g, np.ones(m), 'valid'))
        h = 1-g
        h[i:i+m] = 1
        return np.dot(np.transpose(c),h).item()

# https://leetcode.com/problems/grumpy-bookstore-owner/discuss/3594613/scala-1-line-solution
# def maxSatisfied(customers: Array[Int], grumpy: Array[Int], minutes: Int): Int =
# (customers zip grumpy).map(n => n._2 * n._1).sliding(minutes).map(_.sum).max + (customers zip grumpy).filter(_._2 == 0).map(_._1).sum

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        s=[*map(mul,c,g)];return reduce(lambda t,i:(t,w:=sum(s[i:i+m]))[w>t],range(len(c)-m+1),0)+sum(map(mul,c,map(not_,g)))

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        s,t=[*map(mul,c,g)],0;[t:=(t,w:=sum(s[i:i+m]))[w>t]for i in range(len(c)-m+1)];return t+sum(map(mul,c,map(not_,g)))

class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        return max(__import__('numpy').convolve([*map(mul,c,g)],[1]*m))+sum(map(mul,c,map(not_,g)))

test('''
1052. Grumpy Bookstore Owner
Medium

1982

177

Add to List

Share
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
 

Other examples:

Input: customers = [3], grumpy = [1], minutes = 1
Output: 3

Input: customers = [2,6,6,9], grumpy = [0,0,1,1], minutes = 1
Output: 17

Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
Accepted
110,811
Submissions
183,081
''')
