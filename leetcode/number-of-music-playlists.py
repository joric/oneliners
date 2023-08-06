from lc import *

# https://leetcode.com/problems/number-of-music-playlists/discuss/1311437/Python-simple-recursive-%2B-cache

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def f(t,p,n,k):
            if t==0:
                return 1 if not p else 0
            if t < p:
                return 0
            a = max(0,(n-p-k))*f(t-1,p,n,k)
            b = p * f(t-1,p-1,n,k) if p else 0
            return (a+b)%(10**9+7)
        return f(goal,n,n,k)

class Solution:
    def numMusicPlaylists(self, n: int, g: int, k: int) -> int:
        return(f:=cache(lambda t,p,n,k:t and t>=p and(max(0,n-p-k)*f(t-1,p,n,k)+p*f(t-1,p-1,n,k))%(10**9+7)or not p))(g,n,n,k)

test('''
920. Number of Music Playlists
Hard

923

95

Add to List

Share
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
 

Constraints:

0 <= k < n <= goal <= 100
''')

