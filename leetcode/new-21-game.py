from lc import *

# TLE
class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        return(f:=cache(lambda x:x<=n if x>=k else sum(f(x+i) for i in range(1,w+1))/w))(0)

class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        p,q,s=1,deque([1]*(n-k+1)),n-k+1;[(p:=s/w,q.append(p),s:=s+p,len(q)>w and(s:=s-q.popleft()))for i in range(k-1,-1,-1)];return n>=k+w and 1 or p

class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        d=[0]*(k+max(w,n)+10);[setitem(d,i,1)for i in range(k,n+1)];m=n-k+1;[(setitem(d,i,m/w),m:=m+d[i]-d[i+w])for i in range(k-1,-1,-1)];return d[0]

class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        m,u,v=[0]*(k+w-n)+[1]*(n-k+1)+[(n-k+1)/w],1/w,1+1/w;[m.append(v*m[-1]-u*m[~w])for i in range(k-1)];return(k==0 or n>=k+w-1)and 1.or m[-1]

class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        return(f:=cache(lambda x:min(n-k+1,w)/w if x==k-1 else 0 if x>n else 1 if x>=k else ((w+1)*f(x+1)-f(x+1+w))/w))(0)

class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        return(f:=cache(lambda x:x<=n if x>=k else min(n-k+1,w)/w if x==k-1 else ((w+1)*f(x+1)-f(x+1+w))/w))(0)

class Solution:
    def new21Game(self, n, k, w):
        return(f:=cache(lambda x:x<=n if x>=k else (min(n-x,w),(w+1)*f(x+1)-f(x+1+w))[x!=k-1]/w))(0)

test('''
837. New 21 Game
Medium

1091

732

Add to List

Share
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

 

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
 

Constraints:

0 <= k <= n <= 10^4
1 <= maxPts <= 10^4
''')

