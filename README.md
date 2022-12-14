## Oneliners

### Tricks

#### Imported modules

Leetcode imports modules as wildcards, so you don't have to specify module names.
The only exception is `bisect.bisect()` because `bisect()` triggers `'module' object is not callable`.

* https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

Leetcode header has `import * from itertools`, so we use `comb()` instead of `itertools.comb()`:

```python
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n+k-1, k*2) % (10**9+7)
```

#### Lambdas

Fictitious (anonymous) lambdas also may be nested. E.g. you can use lambdas as parameters:

* `(lambda a,b,c: code)(a,b,c)` becomes `(lambda a,b,c: code)(lambda a: code, lamda b: code, lambda c: code)`

You can't unpack lambda tuples in Python 3 since [PEP 3113](https://peps.python.org/pep-3113/), however, if your lambda is flat, there is an upgrade path:

* `lambda (x, y): x + y` in Python 2 becomes `lambda xy:(lambda x,y: x+y)(*xy)` in Python 3.

You can also unpack multiple tuples as `lambda xy,ab:(lambda x,y,a,b: x+y+a+b)(*(xy+ab))`.

#### Generators

Comprehension generators `(x for y in z)` are memory efficient since they only require memory for
the one value they yield. If you don't care about memory you can use square brackets to run the loop.
You can also exhaust a generator using `all()` or `any()` depending on the return values.
You can also save a few chars using `[*g]` syntax instead of `list(g)` when g is a function.
Generator length can be calculated as `sum(1 for _ in g)` (longer than `len(list(g))` but uses constant memory).

#### While

While loops are not very onliner-friendly. You can use  `count()` generator with `next()` or `takewhile()`
(the latter is also a generator, so you need to run it, i.e. with `any()` and `repeat(0)`).

* https://leetcode.com/problems/sliding-window-maximum/

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r, d = [], deque()
        for i, n in enumerate(nums):
            while d and n>=nums[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.popleft()
            r.append(nums[d[0]])
        return r[k-1:]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return (d:=deque()) or reduce(lambda r,p:(
            next(_ for _ in count() if not(d and p[1]>=nums[d[-1]] and d.pop())),
            d.append(p[0]), d[0]==p[0]-k and d.popleft(), r.append(nums[d[0]])) and r,
            enumerate(nums), [])[k-1:]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return (d:=deque()) or reduce(lambda r,p:(
            any(takewhile(lambda _:d and p[1]>=nums[d[-1]] and d.pop(), repeat(0))),
            d.append(p[0]), d[0]==p[0]-k and d.popleft(), r.append(nums[d[0]])) and r,
            enumerate(nums), [])[k-1:]

```

#### next

Use `next` whether you need a loop with an early exit. Use `count()` generator for infinite loops.
Note that `next` default parameter gets initialized first so you can use it for the startup code.

* https://leetcode.com/problems/two-sum

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            if target-x in seen:
                return seen[target-x], i
            seen[x] = i
        return False

class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        return next((((m[t-x],i) for i,x in enumerate(nums) if t-x in m or m.__setitem__(x,i))),m:={})
```

* https://leetcode.com/problems/break-a-palindrome/discuss/1481905/Python-3-one-line

```python
class Solution:
    def breakPalindrome(self, s: str) -> str:
        for i in range(len(s) // 2):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i + 1:]
        return s[:-1] + 'b' if s[:-1] else ''

class Solution:
    def breakPalindrome(self, s: str) -> str:
        return next((s[:i]+'a'+s[i+1:] for i in range(len(s)//2) if s[i]!='a'), s[:-1] and s[:-1]+'b')
```
* https://leetcode.com/problems/construct-target-array-with-multiple-sums

```python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        return (s:=sum(target),q:=[-a for a in target],heapify(q)) and next((x==1 for _ in count()
            if (x:=-heappop(q))==1 or s==x or (d:=1+(x-1)%(s-x))==x or not (s:=s-x+d,heappush(q,-d))),1)
```

Use `next`, element index, default value and conjunction to update the first element that matches a predicate.

```python
(i:=next((i+1 for i,x in enumerate(v) if pred(x)), 0)) and v.__setitem__(i-1, val)

```

#### map

You can use `map` to traverse through adjacent cells.

* https://leetcode.com/problems/max-area-of-island

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + sum(map(dfs,(i+1,i,i-1,i),(j,j+1,j,j-1)))
            return 0
        return max(dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])))

class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        return max((f:=lambda i,j:g[i].__setitem__(j,0) or 1 + sum(map(f,(i+1,i,i-1,i),(j,j+1,j,j-1)))
            if 0<=i<len(g) and 0<=j<len(g[0]) and g[i][j] else 0)(i,j)
            for i in range(len(g)) for j in range(len(g[0])))
```

Though it's shorter to use complex numbers for 2d maps.

* https://leetcode.com/problems/max-area-of-island/discuss/108565/4-lines

```python
class Solution:
    def maxAreaOfIsland(self, grid):
        grid = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
        def area(z):
            return grid.pop(z, 0) and 1 + sum(area(z + 1j**k) for k in range(4))
        return max(map(area, set(grid)))

class Solution:
    def maxAreaOfIsland(self, grid):
        return max(map(a:=lambda z: g.pop(z, 0) and 1 + sum(a(z + 1j**k) for k in range(4)),
            set(g:= {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)})))
```

* https://leetcode.com/problems/number-of-islands

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = {i + j*1j:int(val) for i,row in enumerate(grid) for j,val in enumerate(row)}
        def f(z):
            return grid.pop(z,0) and bool([f(z + 1j**k) for k in range(4)])
        return sum(map(f, set(grid)))

class Solution:
    def numIslands(self, grid):
        return sum(map(f:=lambda z:g.pop(z,0) and bool([f(z + 1j**k) for k in range(4)]),
            set(g:={i + j*1j:int(x) for i,row in enumerate(grid) for j,x in enumerate(row)})))
```

* https://leetcode.com/problems/unique-paths-iii

```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def f(z,r):
            if x:=g.pop(z,0):
                if x==3 and not g:
                    r = r + 1
                for k in range(4):
                    r = f(z + 1j**k, r)
                g.update({z:x})
            return r
        g = {i + j*1j:x+1 for i, row in enumerate(grid) for j,x in enumerate(row) if x!=-1}
        return f(next(z for z,x in g.items() if x==2),0)

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        return (g:={i + j*1j:x+1 for i, row in enumerate(grid) for j,x in enumerate(row)
        if x!=-1}) and (f:=lambda z,r:[(x:=g.pop(z,0)) and (x==3 and not g and (r:=r+1),
        [r:=f(z + 1j**k,r) for k in range(4)],g.update({z:x}))] and r)
        (next(z for z,x in g.items() if x==2), 0)

```

#### Walrus operator

Use walrus operator (:=) if you need to define or update a variable or a function that's used repeatedly.

* https://leetcode.com/problems/guess-number-higher-or-lower

```python
class Solution(object):
    def guessNumber(self, n: int) -> int:
        l,r = 1, n
        while l <= r:
            m = (l + r) // 2
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

* https://leetcode.com/problems/reverse-integer

```python
class Solution:
    def reverse(self, x: int) -> int:
        r, x = 0, abs(x)
        while x:
            r = r*10 + x%10
            x //= 10
        return ((x>0)-(x<0))*min(2**31, r)

class Solution:
    def reverse(self, x: int) -> int:
        return ((x>0)-(x<0))*min(2**31,(f:=lambda r,x:f(r*10 + x%10, x//10) if x else r)(0,abs(x)))
```

* https://leetcode.com/problems/top-k-frequent-words/discuss/573662/Python-2-lines-heap/1650650

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return nsmallest(k, (f:=Counter(words)).keys(), key=lambda x:(-f[x],x))
```

#### getitem

Used to construct a bisect comparator object, now we have the key parameter (since Python 3.10).

* https://leetcode.com/problems/guess-number-higher-or-lower

```python
class Solution:
    def guessNumber(self, n: int) -> int:        
        return bisect_left(type('',(),{'__getitem__':lambda _,i: -guess(i)})(), 0, 1, n)

class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 0, key=lambda num: -guess(num))
```

#### cache

Cache decorator may be used as an inline function `cache(lambda ...)` in oneliners.

* https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/2555929/python-oneliner-dfs-with-a-cache-decorator

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i, k, sell):
            return 0 if k==0 or i==len(prices) \
            else max(dfs(i+1, k-1, 0) + prices[i], dfs(i+1, k, 1)) if sell \
            else max(dfs(i+1, k, 1)-prices[i], dfs(i+1, k, sell))
        return dfs(0, k, 0)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return (f:=cache(lambda i,k,s:0 if k==0 or i==len(prices)
            else max(f(i+1,k-s,1-s)+prices[i]*(2*s-1),f(i+1,k,s))))(0,k,0)
```

* https://leetcode.com/problems/coin-change

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(n):
            return min([1 + f(n-c) for c in coins]) if n>0 else 0 if n==0 else inf
        x = f(amount)
        return x if x!=inf else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return (lambda x:x if x!=inf else -1)((f:=cache(lambda n:
            min([1+f(n-c) for c in coins]) if n>0 else 0 if n==0 else inf))(amount))
```

#### reduce

Use it to flatten a loop.

* https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1006208/python-oneliner-hashmap

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        start, res, h = 0, 0, {}
        for i, c in enumerate(s):
            start = max(start, h.get(c,0))
            res = max(res, i - start + 1)
            h[c] = i + 1
        return res

class Solution:
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
        return reduce(lambda a,b:(s:=max(a[0],a[2].get(b[1],0)),max(a[1],b[0]-s+1),
            {**a[2],b[1]:b[0]+1}),enumerate(s),(0,0,{}))[1]


class Solution:
    def lengthOfLongestSubstring(self, s):
        return reduce(lambda a,b:(lambda t,r,h,i,c:(s:=max(t,h.get(c,0)),max(r,i-s+1),
            {**h,c:i+1}))(*a,*b),enumerate(s),(0,0,{}))[1]
```

Another example:

* https://leetcode.com/problems/longest-valid-parentheses/

```python
class Solution:
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

#### setattr

Use `__setattr__` (or `__setitem__` for indexes) if you need an assignment (this function returns None).

* https://leetcode.com/problems/add-one-row-to-tree/discuss/764593/Python-7-lines

```python
class Solution:
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
        root.__setattr__('left', self.addOneRow(root.left, v, d - 1, True)) or \
        root.__setattr__('right', self.addOneRow(root.right, v, d - 1, False)) or root if root else None
```

* https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/discuss/1685130/Python-Recursive-with-comments

```python
class Solution(object):
    def deleteMiddle(self, head):
        def f(a, b):
            if not b:
                return a.next
            a.next = f(a.next, b.next.next) if b.next else f(a.next, b.next)
            return a
        return f(head, head.next)

class Solution(object):
    def deleteMiddle(self, head):
        return (f:=lambda a,b:a.__setattr__('next', f(a.next, b.next.next) if b.next
            else f(a.next, b.next)) or a if b else a.next)(head, head.next)
```

Note that `__setitem__` also supports slices:

* https://leetcode.com/problems/count-primes/discuss/111420/Python3-solution-using-Sieve-of-Eratosthenes-time-is-O(n)

```python
class Solution:
    def countPrimes(self, n):
        a = [0,0]+[1]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if a[i]:
                a[i*i:n:i] = [0]*len(a[i*i:n:i])
        return sum(a)

class Solution:
    def countPrimes(self, n):
        return sum(reduce(lambda a,i:a[i] and a.__setitem__(slice(i*i,n,i),[0]*len(a[i*i:n:i])) or a,
            range(2,int(n**0.5)+1), [0,0]+[1]*(n-2)))
```

#### Misc

* Note `itemgetter(n)` is the same length or shorter than `lambda x:x[n]` but a little bit clearer to read.
* You can replace `0 if x==y else z` with `x-y and z`, it's a little bit counterintuitive, but much shorter.

Example:

* https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/616818/Python-4-liner-DFS%2BMemoization

```python
class Solution:
    def jobScheduling(self, s: List[int], endTime: List[int], profit: List[int]) -> int:
        return (a:=sorted(zip(startTime,endTime,profit))) and (f:=cache(lambda i:0 if i==len(a) else
            max(f(bisect_left(a,a[i][1],key=lambda x:x[0]))+a[i][2],f(i+1))))(0)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        return (a:=sorted(zip(startTime,endTime,profit))) and (f:=cache(lambda i:i-len(a) and
            max(f(bisect_left(a,a[i][1],key=itemgetter(0)))+a[i][2],f(i+1))))(0)

```

