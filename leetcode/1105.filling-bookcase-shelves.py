from lc import *

# https://leetcode.com/problems/filling-bookcase-shelves/discuss/541711/Python-3-using-lru_cache-4-lines

class Solution:
    def minHeightShelves(self, b: List[List[int]], w: int) -> int:
        @cache
        def f(i,x,h):
            if i>=len(b):
                return h
            p,q = b[i]
            if x<p:
                return h+f(i+1,w-p,q)
            if h<q:
                return min(h+f(i+1,w-p,q), f(i+1,x-p,q))
            return f(i+1,x-p,h)
        return f(0,w,0)

class Solution:
    def minHeightShelves(self, b: List[List[int]], w: int) -> int:
        return(f:=cache(lambda i,x,h:b[i:]and((p:=b[i][0],q:=b[i][1])and(h+f(i+1,w-p,q)if x<p else(min(f(i+1,x-p,q),h+f(i+1,w-p,q))if h<q else f(i+1,x-p,h))))or h))(0,w,0)

test('''
1105. Filling Bookcase Shelves
Medium

1937

151

Add to List

Share
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

 

Example 1:


Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
Example 2:

Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4
 

Constraints:

1 <= books.length <= 1000
1 <= thicknessi <= shelfWidth <= 1000
1 <= heighti <= 1000
Accepted
64,546
Submissions
104,659
''')