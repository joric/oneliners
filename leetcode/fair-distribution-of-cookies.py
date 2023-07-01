from lc import *

class Solution:
    def distributeCookies(self, c: List[int], k: int) -> int:
        r = [inf]
        d = [0]*k
        def f(i): 
            if i == len(c): 
                r[0] = min(r[0], max(d))
                return 
            if r[0] <= max(d):
                return 
            for j in range(k):
                d[j] += c[i]
                f(i+1)
                d[j] -= c[i]
        if k == len(c): 
            return max(c)
        f(0)
        return r[0]

class Solution:
    def distributeCookies(self, c: List[int], k: int) -> int:
        d = [0] * k
        def f(i,m):
            if i==len(c):
                return m
            r = inf
            for j in range(k):
                d[j] += c[i]
                r = min(r,f(i+1,max(m,d[j])))
                d[j] -= c[i]
            return r
        if k == len(c): 
            return max(c)
        return f(0,0)

class Solution:
    def distributeCookies(self, c: List[int], k: int) -> int:
        d,f=Counter(),lambda i,m,r=inf:m if i==len(c) else [(d.update({j:c[i]}),r:=min(r,f(i+1,max(m,d[j]))),d.update({j:-c[i]})) for j in range(k)]and r;return max(c) if k==len(c) else f(0,0)

class Solution:
    def distributeCookies(self, c: List[int], k: int) -> int:
        d,n,f=Counter(),len(c),lambda i,m,r=inf:(i==n or k==n)and m or[(d.update({j:c[i]}),r:=min(r,f(i+1,max(m,d[j]))),d.update({j:-c[i]}))for j in range(k)]and r;return f(0,max(c))

test('''
2305. Fair Distribution of Cookies
Medium

905

43

Add to List

Share
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

 

Example 1:

Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.
Example 2:

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.


Input: cookies=[1,1,2,2,2,3,4,6], k = 3
Output: 7

Constraints:

2 <= cookies.length <= 8
1 <= cookies[i] <= 10^5
2 <= k <= cookies.length
Accepted
24,651
Submissions
39,916
Seen this question in a real interview before?

Yes

No
We have to give each bag to one of the children. How can we enumerate all of the possibilities?
Use recursion and keep track of the current number of cookies each child has. Once all the bags have been distributed, find the child with the most cookies.
''')

