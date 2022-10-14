## Oneliners

### Tricks

#### Imported modules

Leetcode imports modules as wildcards, so you don't have to specify module names.
The only exception is `bisect.bisect()` because `bisect()` triggers `'module' object is not callable`.

* https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

Leetcode header has `import * from itertools`, so we use `comb()` instead of `itertools.comb()`:

```python
class Solution: numberOfSets = lambda _,n,k: comb(n+k-1,k*2) % (10**9+7)
```

#### lambdas

Fictitious (anonymous) lambdas also may be nested. E.g. `(lambda a,b,c: code)(a,b,c)`
can use lambdas as parameters `(lambda a,b,c: code)(lambda a: code, lamda b: code, lambda c: code)`. No example just yet.

#### walrus operator

Use walrus operator (:=) if you need to define a lambda function that's called multiple times in the code.

* https://leetcode.com/problems/deepest-leaves-sum

```python
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return (dfs:=lambda node,i:0 if not node \
        else dfs(node.left,i-1) + dfs(node.right,i-1) if i else node.val) \
        (root,(level:=lambda node:max(level(node.left),level(node.right))+1 if node else 0)(root)-1)
```

* https://leetcode.com/problems/guess-number-higher-or-lower

```python
class Solution1(object):
    def guessNumber(self, n):
        l,r = 1, n
        while l <= r:
            m = (l + r) / 2
            res = guess(m)
            if res == 0:
                return m
            elif res > 0:
                l = m + 1
            else:
                r = m - 1
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        return (f:=lambda l,h:h if l+1==h else f(m,h) if guess(m:=(l+h)//2)>0 else f(l,m))(0,n)
```

#### getitem

You can use it to construct a bisect comparator object (but we have the key parameter now).

* https://leetcode.com/problems/guess-number-higher-or-lower

```python
class Solution1:
    def guessNumber(self, n: int) -> int:        
        return bisect_left(type('',(),{'__getitem__':lambda _,i: -guess(i)})(), 0, 1, n)

class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 0, key=lambda num: -guess(num))
```

#### cache

Cache decorator may be used as an inline function `cache(fn)` in oneliners.

* https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/2555929/python-oneliner-dfs-with-a-cache-decorator

```python
class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i, k, sell):
            return 0 if k==0 or i==len(prices) \
            else max(dfs(i+1, k-1, 0) + prices[i], dfs(i+1, k, 1)) if sell \
            else max(dfs(i+1, k, 1)-prices[i], dfs(i+1, k, sell))
        return dfs(0, k, 0)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return (f:=cache(lambda i,k,s:0 if k==0 or i==len(prices) \
            else max(f(i+1,k-s,1-s)+prices[i]*(2*s-1),f(i+1,k,s))))(0,k,0)
```

#### reduce

Use it to flatten a loop.

* https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1006208/python-oneliner-hashmap

```python
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        start, res, h = 0, 0, {}
        for i, c in enumerate(s):
            start = max(start, h.get(c,0))
            res = max(res, i - start + 1)
            h[c] = i + 1
        return res

class Solution2:
    def lengthOfLongestSubstring(self, s):
        def fn(a,b):
            start, res, h = a
            i, c = b
            start = max(start, h.get(c,0))
            res = max(res, i - start + 1)
            h[c] = i + 1
            return start,res,h
        return reduce(fn,enumerate(s),[0,0,{}])[1]

class Solution:
    def lengthOfLongestSubstring(self, s):
        return reduce(lambda a,b:(s:=max(a[0],a[2].get(b[1],0)),max(a[1],b[0]-s+1),\
            {**a[2],b[1]:b[0]+1}),enumerate(s),(0,0,{}))[1]
```

Another example:

* https://leetcode.com/problems/longest-valid-parentheses/

```python
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        def fn(a,b):
            r, s = a
            i, p = b
            return (max(r,i-s[-2][0]), s[:-1]) if p==')' and s[-1][1]=='(' else (r, s+[(i,p)])
        return reduce(fn, enumerate(s), (0,[(-1, ')')]))[0]

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return reduce(lambda a,b:(max(a[0],b[0]-a[1][-2][0]),a[1][:-1]) if b[1]==')'
            and a[1][-1][1]=='(' else (a[0],a[1]+[b]),enumerate(s),(0,[(-1,')')]))[0]
```

#### next

Use `next` whether you need an oneliner loop with an early exit.

* https://leetcode.com/problems/break-a-palindrome/discuss/1481905/Python-3-one-line

```python
class Solution1:
    def breakPalindrome(self, s: str) -> str:
        for i in range(len(s) // 2):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i + 1:]
        return s[:-1] + 'b' if s[:-1] else ''

class Solution:
    def breakPalindrome(self, s: str) -> str:
        return next((s[:i]+'a'+s[i+1:] for i in range(len(s)//2) if s[i]!='a'), s[:-1] and s[:-1]+'b')
```

#### setattr

Use `__setattr__` (or `__setitem__` for indexes) if you need an assignment (this function returns None).

* https://leetcode.com/problems/add-one-row-to-tree/discuss/764593/Python-7-lines

```python
class Solution1:
    def addOneRow(self, root: TreeNode, v: int, d: int, isLeft: bool = True) -> TreeNode:
        if d == 1:
        return TreeNode(v, root if isLeft else None, root if not isLeft else None)
        if not root:
        return None
        root.left = self.addOneRow(root.left, v, d - 1, True)
        root.right = self.addOneRow(root.right, v, d - 1, False)
        return root

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int, isLeft: bool = True) -> TreeNode:
        return TreeNode(v, root if isLeft else None, root if not isLeft else None) if d==1 else \
        root.__setattr__("left",self.addOneRow(root.left, v, d - 1, True)) or \
        root.__setattr__("right",self.addOneRow(root.right, v, d - 1, False)) or root if root else None
```

* https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/discuss/1685130/Python-Recursive-with-comments

```python

class Solution1(object):
    def deleteMiddle(self, head):
        def f(a, b):
            if not b:
                return a.next
            a.next = f(a.next, b.next.next) if b.next else f(a.next, b.next)
            return a
        return f(head, head.next)

class Solution(object):
    def deleteMiddle(self, head):
        return (f:=lambda a,b:a.__setattr__('next', f(a.next, b.next.next) if b.next \
        else f(a.next, b.next)) or a if b else a.next)(head, head.next)
```

#### map

You can use `map` to traverse through adjacent cells.

* https://leetcode.com/problems/max-area-of-island

```python
class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + sum(map(dfs,(i+1,i,i-1,i),(j,j+1,j,j-1)))
            return 0
        return max(dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])))

class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        return max((f:=lambda i,j:g[i].__setitem__(j,0) or 1 + sum(map(f,(i+1,i,i-1,i),(j,j+1,j,j-1)))\
        if 0<=i<len(g) and 0<=j<len(g[0]) and g[i][j] else 0)(i,j)\
        for i in range(len(g)) for j in range(len(g[0])))
```

It's shorter to use complex numbers for 2d maps.

* https://leetcode.com/problems/max-area-of-island/discuss/108565/4-lines

```python
class Solution1:
    def maxAreaOfIsland(self, grid):
        grid = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
        def area(z):
            return grid.pop(z, 0) and 1 + sum(area(z + 1j**k) for k in range(4))
        return max(map(area, set(grid)))

class Solution:
    def maxAreaOfIsland(self, grid):
        return max(map((g:= {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)},\
        a:=lambda z: g.pop(z, 0) and 1 + sum(a(z + 1j**k) for k in range(4)))[1], set(g)))

```

