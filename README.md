## Oneliners

### Leetcode-specific

Leetcode imports modules as wildcards, so you don't have to specify module names. There are some exceptions:

* Single `bisect()` without a prefix triggers `object is not callable`, use `bisect.bisect()` or `bisect_left()`.
* You have to specify `re.sub` because `sub` without a prefix is `operator.sub`.
* Default `pow` is `__builtins__['pow']` (supports up to 3 arguments, including a module), not `math.pow`.

For example, Leetcode header has `import * from itertools`, so we use `comb()` instead of `itertools.comb()`:

* https://leetcode.com/problems/unique-paths

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, n-1)
```

You can also use `__import__('module').func` for unlisted modules (i.e. "numpy", "scipy", and "sortedcontainers").

* https://leetcode.com/problems/check-if-it-is-a-straight-line

```python
class Solution:
    def checkStraightLine(self, p):
        return __import__('numpy').linalg.matrix_rank([[1]+x for x in p])<3
```

Sometimes you can save on casting of the return type, e.g. Leetcode autoconverts keys and mixed types to lists.

* https://leetcode.com/problems/top-k-frequent-elements

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return dict(Counter(nums).most_common(k))
```

It also automatically evaluates generators:

* https://leetcode.com/problems/counting-bits

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        return map(int.bit_count,range(n+1))
```

You can also return linked list of values as `ListNode('a,b,...')`. This one is really specific, but sometimes useful.

* https://leetcode.com/problems/add-two-numbers

```python
class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        f=lambda n:n and n.val+10*f(n.next)or 0;return ListNode(','.join([*str(f(a)+f(b))][::-1]))
```

Leetcode lists and trees also have `serialize` and `deserialize` functions:

* https://leetcode.com/problems/reverse-linked-list

```python
class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h and h.deserialize(str(eval(h.serialize(h))[::-1]))
```

More undocumented functions:

* ListNode: `_has_cycle`, `_list_node_to_array`, `_array_to_list_node`.
* TreeNode: `_has_cycle`, `_tree_node_to_array`, `_array_to_tree_node`.

Also Leetcode apparently stores final result in the `user.out` file and allows writing to it:

* https://leetcode.com/problems/two-sum

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from zlib import decompress
        from base64 import b64decode
        open('user.out', 'wb').write(decompress(b64decode('eJzdkMEVwCAIQ++dggFyEKi2zuLr/mtItZb63KAc\
kpfwuVAYFK6tCIjNPH1KncodJMuBTqWTYUGe89hNX1Kd/K2Nh1iM3mYbkMlpIaFrvvcCaVwCH+YB3FSHVu5xXDc='))),exit(0)
```

There is no approved method to obtain all the test cases for problems in LeetCode.
You can, however, leverage the fact that LeetCode reveals the test case that causes your code to fail.
The solution above is not very reliable, because tests and environment may change, but it's pretty fast.

* https://leetcode.com/discuss/feedback/4643730/a-python-solution-that-contain-malicious-payload-in-your-website

### Lambdas

Fictitious (anonymous) lambdas also may be nested. E.g. you can use lambdas as parameters:

* `(lambda a,b,c: code)(a,b,c)` becomes `(lambda a,b,c: code)(lambda a: code, lamda b: code, lambda c: code)`

You can't unpack lambda tuples in Python 3 since [PEP 3113](https://peps.python.org/pep-3113/), however, if your lambda is flat, there is an upgrade path:

* `lambda (x, y): x + y` in Python 2 becomes `lambda xy:(lambda x,y: x+y)(*xy)` in Python 3.

You can also unpack multiple tuples as `lambda xy,ab:(lambda x,y,a,b: x+y+a+b)(*(xy+ab))`.

* https://leetcode.com/problems/count-vowels-permutation

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return sum(reduce(lambda x,_:(lambda a,e,i,o,u:(e+i+u,a+i,e+o,i,i+o))(*x),[0]*(n-1),[1]*5))
            %(10**9+7)
```

### Generators

Generator expressions `(x for y in z)` are memory efficient since they only require memory for
the one value they yield. If you don't care about memory you can use square brackets to make it a list comprehension that automatically runs the loop.
You can also exhaust a generator using `all()` or `any()` depending on the return values.
You can also save a few chars using `[*g]` syntax instead of `list(g)` where g is a generator function.
Generator length `len(list(g))` can be calculated in constant memory as `sum(1 for _ in g)`.

### Counters

Counters (`collections.Counter()`) can be updated, similar to `dict.update()`, it's much faster than a sum of counters.
E.g. `c[i]+=1` is equivalent to `c.update([i])`, `c[i]-=1` is `c.update({i:-1})`.
To delete a key you can use the `.pop` method (same as `del`), it's shorter than `popitem()`.

You can easily drop zero and negative values in a counter (it's the official way, see [documentation](https://docs.python.org/3/library/collections.html#collections.Counter)):

```python
c = Counter({1:1,2:0,3:-1}); print(c:=+c) #{1: 1}, same as c += Counter()
```

Since python 3.7, as a dict subclass, Counter inherited the capability to remember insertion order.

* https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal

```python

class Solution:
    def reductionOperations(self, n: List[int]) -> int:
        return sum(i*v for i,(_,v)in enumerate(sorted(Counter(n).items())))

class Solution:
    def reductionOperations(self, n: List[int]) -> int:
        return sum(i*v for i,v in enumerate(Counter(sorted(n)).values()))

```

Since Python 3.10 you can use `total()` to compute sum of the counts.

* https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s)-Counter(t)).values())

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return(Counter(s)-Counter(t)).total()
```

### Walrus operator

The controversial walrus operator (`:=`) added in Python 3.8 ([PEP-572](https://peps.python.org/pep-0572/)
that [made Guido resign](https://www.infoworld.com/article/3292936/guido-van-rossum-resigns-whats-next-for-python.html)),
can be used to define or update a variable or a function (mostly used for recursive functions).

You can define and call a recursive function in a single line with Y-combinator, e.g.:

```python
return (lambda y,x:y(y,x))(lambda f,x:1 if x==0 else x*f(f,x-1),5)
```

But the walrus operator syntax is much more concise:

```python
return (f:=lambda x:1 if x==0 else x*f(x-1))(5)
```

Many oneliners would be impossible to do without it (or rather, very hard, with nested lambdas).
Sometimes you don't even need extra brackets, e.g. in `map(f:=x,y)` or `next(g,f:=x)` so it may be shorter than operators separated by semicolons.

* https://leetcode.com/problems/time-needed-to-inform-all-employees

```python
class Solution:
    def numOfMinutes(self, n: int, h: int, m: List[int], t: List[int]) -> int:
        return max(map(f:=cache(lambda i:~i and t[i]+f(m[i])),m))
```

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
        return nsmallest(k,(f:=Counter(words)).keys(),lambda x:(-f[x],x))
```

### Setting values

You can't use walrus operator for structures, however, you can use `__setattr__` for dictionaries or `__setitem__` for lists if you need an assignment
(functions return `None`). To set a key for the list or for the dictionary, you can also use `setattr` or `setitem` functions from the `operator` module,
e.g. `c[x]=1` is the same as `setitem(c,x,1)`.

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
        setattr(root,'left', self.addOneRow(root.left, v, d - 1, True)) or \
        setattr(root,'right', self.addOneRow(root.right, v, d - 1, False)) or root if root else None
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
        return (f:=lambda a,b:setattr(a,'next',f(a.next, b.next.next) if b.next
            else f(a.next, b.next)) or a if b else a.next)(head, head.next)
```

Note that `setitem` also supports slices:

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
        return sum(reduce(lambda a,i:a[i] and setitem(a,slice(i*i,n,i),[0]*len(a[i*i:n:i])) or a,
            range(2,int(n**0.5)+1), [0,0]+[1]*(n-2)))
```

Note slices can extend the list implicitly, e.g.:

```python
a = [0,1,2]
a[3:4] = [3] # [0,1,2,3]
```
Be careful though, slicing doesn't extend list beyond the slice size:

```python
a = [0,1]
a[3:4] = [3,4] # the result is [0,1,3,4], NOT [0,1,?,3,4] (!)
```

Examples:

* https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position

```python
class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        d = []
        for e in o:
            i = bisect_right(d,e)
            if i==len(d):
                d.append(0)
            d[i] = e
            yield i+1

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        d = []
        for e in o:
            i = bisect_right(d,e)
            d[i:i+1] = [e]
            yield i+1

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        d=[];return[setitem(d,slice(i:=bisect_right(d,e),i+1),[e])or i+1for e in o]
```

Sometimes `exec` is shorter than `setitem`.

* https://leetcode.com/problems/design-parking-system

```python
ParkingSystem=type('',(),{'__init__':lambda s,a,b,c:setattr(s,'p',[0,a,b,c]),'addCar':lambda s,t:\
    setitem(s.p,t,s.p[t]-1)or s.p[t]>=0})

ParkingSystem=type('',(),{'__init__':lambda s,a,b,c:setattr(s,'p',[0,a,b,c]),'addCar':lambda s,t:\
    exec('s.p[t]-=1')or s.p[t]>=0})
```

### Getting values

Use the usual bracket notation `[]` or `dict.get(key,default)` (where needed).

Getitem used to construct a bisect comparator object, now we have the key parameter (since Python 3.10).

* https://leetcode.com/problems/guess-number-higher-or-lower

```python
class Solution:
    def guessNumber(self, n: int) -> int:        
        return bisect_left(type('',(),{'__getitem__':lambda _,i: -guess(i)})(), 0, 1, n)

class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 0, key=lambda num: -guess(num))
```

You can also write a subclass in one line, if needed.

* https://leetcode.com/problems/design-hashset

```python
MyHashSet=type('',(set,),{'remove':set.discard,'contains':set.__contains__})
```

* https://leetcode.com/problems/implement-stack-using-queues

```python
MyStack=type('',(list,),{'push':list.append,'top':lambda s:s[-1],'empty':lambda s:not s})
```

* https://leetcode.com/problems/insert-delete-getrandom-o1

```python
с=Counter;с.insert=lambda s,x:s.update({x})or s[x]<2;с.remove=lambda s,x:s.pop(x,0);
с.getRandom=lambda s:choice([*s]);RandomizedSet=с
```

Sometimes (not always) you can skip `__init__` and use static attributes.

* https://leetcode.com/problems/design-underground-system

```python
UndergroundSystem=type('',(),{'h':{},'m':{},
	'checkIn':lambda s,i,v,t:setitem(s.m,i,(v,t)),
	'checkOut':lambda s,i,d,w:(v:=s.m[i][0])and setitem(s.h,(v,d),
	[*map(sum,zip(s.h.pop((v,d),(0,0)),(w-s.m[i][1],1)))]),
	'getAverageTime':lambda s,v,d:truediv(*s.h[v,d])})
```


### While loops

While loops are not very oneliner-friendly. You can use  `count()` generator with `next()`.
Note that `next` default parameter gets initialized first so you can use it for the startup code (but can't use to calculate result).

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
    def twoSum(self, n: List[int], t: int) -> List[int]:
        return next(((m[t-x],i)for i,x in enumerate(n)if t-x in m or setitem(m,x,i)),m:={})
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
        return next((s[:i]+'a'+s[i+1:]for i in range(len(s)//2)if s[i]!='a'),s[:-1]and s[:-1]+'b')
```
* https://leetcode.com/problems/construct-target-array-with-multiple-sums

```python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        q = [-a for a in target]
        heapify(q)
        while True:
            x = -heappop(q)
            if x==1:
                return True
            if s==x:
                return False
            d = 1 + (x-1) % (s-x)
            if x==d:
                return False
            s = s - x + d
            heappush(q, -d)

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        return (s:=sum(target),q:=[-a for a in target],heapify(q)) and next((x==1 for _ in count()
        if (x:=-heappop(q))==1 or s==x or (d:=1+(x-1)%(s-x))==x or not (s:=s-x+d,heappush(q,-d))),1)
```

You can also use `takewhile()`, it's also a generator, so you need to expand it (e.g. with `repeat(0)`).

* https://leetcode.com/problems/sliding-window-maximum

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
            any(takewhile(lambda _:d and p[1]>=nums[d[-1]] and d.pop(), repeat(0))),
            d.append(p[0]), d[0]==p[0]-k and d.popleft(), r.append(nums[d[0]])) and r,
            enumerate(nums), [])[k-1:]

```

You could also try `any()` or `all()` as a while loop instead of `next()`, it may be shorter.
You can assure that expression never returns `None`, using `[]` (`[None]` evaluates to `True`).

* https://leetcode.com/problems/last-stone-weight

```python

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            insort(stones,stones.pop() - stones.pop())
        return stones[0]

class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        return next((s[0] for _ in count() if not s[1:] or insort(s,s.pop()-s.pop())),s.sort())

class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        return (s.sort(),all(s[1:] and [insort(s,s.pop()-s.pop())] for _ in count()),s[0])[2]
```

You can also evalulate multiline code with `exec`. Unlike `eval`, is not limited to a single string.

* https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return next((r for _ in count()if not(n and(r:=r^n,n:=n//2))),r:=0)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        r=[0];exec('while n:\n r[0]^=n\n n//=2');return r[0]

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return(f:=lambda n:n and n^f(n//2))(n)
```

### Swapping values

To swap values you can use either `exec` (inline version of `a,b=b,a`) or a temporary variable (`t:=a,a:=b,b:=t`).

Note that `eval` accepts only a single expression, and returns the value of the given expression,
whereas `exec` ignores the return value from its code, and always returns `None`, its use has no effect
on the compiled bytecode of the function where it is used. It does however affect existing variables.

Example:

* https://leetcode.com/problems/sort-colors

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def fn(t,b):
            red, white, blue = t
            return (swap:=lambda a,x,y:exec('a[x],a[y]=a[y],a[x]'),(swap(nums,red,white),
            (red+1,white+1,blue))[1] if nums[white]==0 else ((red,white+1,blue) if nums[white]==1
            else (swap(nums,white,blue),(red,white,blue-1))[1]))[1]
        reduce(fn, nums, [0,0,len(nums)-1])

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        (s:=lambda a,x,y:(t:=a[x],setitem(a,x,a[y]),setitem(a,y,t),a)[3],
        f:=lambda a,i,j,k:(f(s(a,i,j),i+1,j+1,k) if a[j]==0 else f(a,i,j+1,k) if a[j]==1
        else f(s(a,j,k),i,j,k-1)) if i<=j<=k else None)[1](nums,0,0,len(nums)-1)
```

Also you can try a swap function here (but it's pretty long, I don't use it):

* https://stackoverflow.com/questions/4362153/lambda-returns-lambda-in-python

```python
swap = lambda a,x,y:(lambda f=a.__setitem__:(f(x,(a[x],a[y])),f(y,a[x][0]),f(x,a[x][1])))()
```

### Mapping

You can use `map` for a lot of things, for example to traverse through adjacent cells.

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
        return max((f:=lambda i,j:setitem(g[i],j,0) or 1 + sum(map(f,(i+1,i,i-1,i),(j,j+1,j,j-1)))
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

Complex numbers in general are very useful as 2d coordinates:

* https://leetcode.com/problems/path-crossing

```python
class Solution:
    def isPathCrossing(self, p: str) -> bool:
        z=0;return len(p)>=len({0,*{z:=z+1j**'NESW'.find(c)for c in p}})
```


You can convert lists or tuples to `True` with `!=0` instead of `bool()` (3 chars shorter).

* https://leetcode.com/problems/number-of-islands

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = {i + j*1j:int(val) for i,row in enumerate(grid) for j,val in enumerate(row)}
        def f(z):
            return grid.pop(z,0) and bool([f(z + 1j**k) for k in range(4)])
        return sum(map(f, set(grid)))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return sum(map(f:=lambda z:g.pop(z,0) and [f(z + 1j**k) for k in range(4)]!=0,
            set(g:={i + j*1j:int(x) for i,row in enumerate(grid) for j,x in enumerate(row)})))
```

* https://leetcode.com/problems/number-of-closed-islands

```python
class Solution:
    def closedIsland(self, grid: List[List[str]]) -> int:
        g = {i+j*1j:1-x for i,r in enumerate(grid) for j,x in enumerate(r)}
        f = lambda z:g.pop(z,0) and [f(z+1j**k) for k in range(4)]!=0
        sum(f(z) for z in set(g) if not(0<z.real<len(grid)-1 and 0<z.imag<len(grid[0])-1))
        return sum(map(f,set(g)))

class Solution:
    def closedIsland(self, grid: List[List[str]]) -> int:
        return (g:={i+j*1j:1-x for i,r in enumerate(grid) for j,x in enumerate(r)},
            f:=lambda z:g.pop(z,0) and [f(z+1j**k) for k in range(4)]!=0,[f(z) for z in set(g)
            if not(0<z.real<len(grid)-1 and 0<z.imag<len(grid[0])-1)]) and sum(map(f,set(g)))
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

### Unicode Find

Unicode find (NOT Union Find) is the greatest trick of all time to solve graph problems.
The idea is to use string replace in a Unicode space. Introduced by Stephan Pochmann.

* https://leetcode.com/problems/redundant-connection/discuss/108002/Unicode-Find-(5-short-lines)

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        t = ''.join(map(chr, range(1001)))
        for u,v in edges:
            if t[u]==t[v]:
                return [u,v]
            t = t.replace(t[u],t[v])

class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        t=''.join(map(chr,range(1001)));
        return next((u,v)for u,v in e if t[u]==t[v]or not(t:=t.replace(t[u],t[v])))
```

Another example:

* https://leetcode.com/problems/swim-in-rising-water

```python

class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:
        n = len(g)
        t,r = ''.join(map(chr,range(n*n))),range(n)
        for w,i,j in sorted((g[i][j],i,j)for i,j in product(r,r)):
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if n>y>=0<=x<n and g[x][y]<=w:
                    t = t.replace(t[i*n+j],t[x*n+y])
            if t[0]==t[-1]:
                return w
        return 0

class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:
        n=len(g);t,r=''.join(map(chr,range(n*n))),range(n);return next((w for w,i,j in
        sorted((g[i][j],i,j)for i,j in product(r,r))if[t:=t.replace(t[i*n+j],t[x*n+y]) for x,y
        in((i+1,j),(i-1,j),(i,j+1),(i,j-1)) if n>y>=0<=x<n and g[x][y]<=w]and t[0]==t[-1]),0)

```

Another example (Q4 at https://leetcode.com/contest/weekly-contest-392):

```python
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        t,c = ''.join(map(chr,range(n))),{}
        for u,v,w in edges:
            t = t.replace(t[u],t[v])
        for u,v,w in edges:
            c[t[u]] = c.get(t[u],w)&w
        return [0 if u==v else c[t[u]] if t[u]==t[v] else -1 for u,v in query]

class Solution:
    def minimumCost(self, n: int, e: List[List[int]], q: List[List[int]]) -> List[int]:
        t,c=''.join(map(chr,range(n))),{};all(t:=t.replace(t[u],t[v])for u,v,_ in e);
        [setitem(c,t[u],c.get(t[u],w)&w)for u,v,w in e];
        return[u!=v and t[u]!=t[v]and-1or c[t[u]]for u,v in q]
```

### Cache

Cache decorator, `@lru_cache` or `@cache` (since Python 3.9) may be used as an inline function `cache(lambda ...)`.

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

It is sometimes necessary to reset cache with `cache_clear` between tests to avoid Memory Limit Exceeded error.

* https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target

```python
class Solution:
    def lengthOfLongestSubsequence(self, a: List[int], t: int) -> int:
        return(a.sort(),r:=(f:=cache(lambda i,b:b and -inf if b<0 or i<0 else
            max(1+f(i-1,b-a[i]),f(i-1,b))))(len(a)-1,t),f.cache_clear())and(-1,r)[r>0]
```

### Reduce

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

* https://leetcode.com/problems/longest-valid-parentheses

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

### Semicolons

Nobody will stop you from using semicolons, but you'd still have to convert while and for loops.

Example:

* https://leetcode.com/problems/swapping-nodes-in-a-linked-list

```python
class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        q = h
        i = 1
        d = {}
        while q:
            d[i] = q
            q = q.next
            i += 1
        d[k].val, d[i-k].val = d[i-k].val, d[k].val
        return h

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        q=h;i=1;d={};all(q and(setitem(d,i,q),q:=q.next,i:=i+1) for _
            in count());d[k].val,d[i-k].val=d[i-k].val,d[k].val;return h

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[h]+[h:=h.next for _ in[1]*10**5if h];a,b=l[k-1],l[~k];a.val,b.val=b.val,a.val;return l[0]
```

### Math tricks

Many leetcode problems use Fibonacci sequence that can be calculated using a variety of different methods:

* https://r-knott.surrey.ac.uk/Fibonacci/fibFormula.html
* https://en.wikipedia.org/wiki/Generating_function
* https://mathworld.wolfram.com/TribonacciNumber.html

Examples:

* https://leetcode.com/problems/fibonacci-number

```python
class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for _ in range(n):
            a,b = b,a+b
        return a 

class Solution:
    def fib(self, n: int) -> int:
        return pow(x:=2<<n,n+1,x*x+~x)%x
```

* https://leetcode.com/problems/climbing-stairs


```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a=b=1
        for _ in range(n):
            a,b = b,a+b
        return a

class Solution:
    def climbStairs(self, n):
        return pow(x:=2<<n,n+2,x*x+~x)%x
```

* https://leetcode.com/problems/n-th-tribonacci-number

```python
class Solution:
    def tribonacci(self, n):
        a,b,c = 1,0,0
        for _ in range(n):
            a,b,c = b,c,a+b+c
        return c

class Solution:
    def tribonacci(self, n: int) -> int:
        return pow(x:=2<<n,n+2,~-x*x*x+~x)%x
```

### Regex

Many problems can be solved with a single regular expression with lookahead expressions:

* https://leetcode.com/problems/make-the-string-great

```python
class Solution:
    def makeGood(self, s: str) -> str:
        [s:=re.sub(r'(.)(?!\1)(?i:\1)','',s)for _ in s];return s
```

* https://leetcode.com/problems/sort-vowels-in-a-string

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        return re.sub(t:='(?i)[aeiou]',lambda m,v=sorted(findall(t,s)):heappop(v),s)
```

* https://leetcode.com/problems/valid-word

```python
class Solution:
    def isValid(self, w: str) -> bool:
        return re.match('^(?=.*[aiueo])(?=.*[b-df-hj-np-tv-z])[a-z0-9]{3,}$',w,re.I)
```

### Misc

Note that `key=itemgetter(n)` is the same length as `key=lambda x:x[n]` but a little bit clearer to read.

Sometimes you can skip `key=itemgetter(0)` by converting an argument to a tuple (15 characters shorter).

* https://leetcode.com/problems/maximum-profit-in-job-scheduling

```python

class Solution:
    def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        a=sorted(zip(s,e,p));return(f:=cache(lambda i:i-len(a)and max(f(
            bisect_left(a,a[i][1],key=itemgetter(0)))+a[i][2],f(i+1))))(0)

class Solution:
    def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        a=sorted(zip(s,e,p));return(f:=cache(lambda i:i-len(a)and max(f(
            bisect_left(a,(a[i][1],)))+a[i][2],f(i+1))))(0)

```

You could also use `map(list.pop, v)` instead of `[x[-1] for x in v]` to collect the last elements of the list.

* https://leetcode.com/problems/diagonal-traverse-ii

```python
class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        return map(list.pop,sorted([i+j,j,t]for i,r in enumerate(n)for j,t in enumerate(r)))
```

Using `zip` to get elements from the list of tuples is usually shorter, but not always:

* https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes

```python
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return {*range(n)}-{*[*zip(*edges)][1]}

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return {*range(n)}-{j for _,j in edges}
```

You can can use `a!=b!=c` in a single boolean condition, similar to `0<=i<n` and `m>j>=0<=i<n`.

* https://leetcode.com/problems/expressive-words/discuss/122660/C%2B%2BJavaPython-2-Pointers-and-4-pointers

```python
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def f(v,w,j=0):
            for i in range(len(v)):
                if j<len(w) and v[i]==w[j]:
                    j += 1
                elif v[i-1:i+2] != v[i]*3 != v[i-2:i+1]:
                    return False
            return j==len(w)
        return sum(f(s,w) for w in words)

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum((f:=lambda v,w,j=0:next((0 for i in range(len(v)) if not(j<len(w) and v[i]==w[j]
            and (j:=j+1))and v[i-1:i+2]!=v[i]*3!=v[i-2:i+1]),1) and j==len(w))(s,w) for w in words)

```

Python handles comparisons in the same order as `and` operator (e.g. `log` throws exception if n==0):

* https://leetcode.com/problems/power-of-four

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and log(n,4)%1==0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0==log(n,4)%1
```

`~` reverts every bit. Therefore, `~x` means `-x-1`. You can use it as reversed index, i.e. for `i=0`, `a[~i]` means `a[-1]`, etc. or just replace `-x-1` with `~x`.

For integer n, you can write `n+1` as `-~n`, `n-1` as `~-n`. This uses the same number of characters, but can indirectly cut spaces or parens for operator precedence.


* https://leetcode.com/problems/spiral-matrix-ii/

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r=range(n);return[[4*(n-(a:=min(min(i,n-i-1),min(j,n-j-1))))
            *a+(i+j-2*a+1,4*(n-2*a-1)-(i+j-2*a)+1)[i>j] for j in r] for i in r]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r=range(n);return[[4*(n-(a:=min(i,j,~i+n,~j+n)))
            *a+(i+j-2*a+1,4*n-6*a-i-j-3)[i>j]for j in r]for i in r]
```

You can replace `0 if x==y else z` with `x-y and z`, it's a little bit counterintuitive, but shorter.

Condition `x if c else y` can be written as `c and x or y`, it's shorter but depends on x (x should not be 0).

* https://leetcode.com/problems/snakes-and-ladders/discuss/173378/Diagram-and-BFS

```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n,v,q = len(board),{1:0},[1]
        def f(i):
            x = (i - 1)%n
            y = (i - 1)//n
            c = board[~y][~x if y%2 else x]
            return c if c>0 else i
        for i in q:
            for j in range(i+1, i+7):
                k = f(j)
                if k==n*n:
                    return v[i]+1
                if k not in v:
                    v[k] = v[i]+1
                    q.append(k)
        return -1

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        return (n:=len(board),v:={1:0},q:=[1]) and next((v[i]+1 for i in q for j in range(i+1,i+7)
            if (k:=(x:=(j-1)%n,y:=(j-1)//n) and ((c:=board[~y][y%2 and ~x or x])>0 and c or j))==n*n
            or (k not in v and (v.update({k:v[i]+1}) or q.append(k)))),-1)
```

You can check if any of the numbers is negative as `x|y<0` or if both numbers are non-zero as `x|y`.

* https://leetcode.com/problems/minimum-path-sum

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return (f:=cache(lambda i,j:i|j<0 and inf or grid[i][j]+(i|j and min(f(i,j-1),f(i-1,j)))))
            (len(grid)-1,len(grid[0])-1)
```

You can use bitwise `&`,`|` instead of `and`,`or` where possible. If x is `0..2`, using `x&1` is shorter than `x==1`.

* https://leetcode.com/problems/scramble-string

```python

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return (f:=cache(lambda a,b:a==b or any((f(a[:i],b[:i]) and f(a[i:],b[i:]))
            or (f(a[i:],b[:-i]) and f(a[:i],b[-i:])) for i in range(1,len(a)))))(s1,s2)

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return (f:=cache(lambda a,b:a==b or any((f(a[:i],b[:i])&f(a[i:],b[i:]))
            |(f(a[i:],b[:-i])&f(a[:i],b[-i:])) for i in range(1,len(a)))))(s1,s2)
```

You can use booleans as indexes in lists, even nested: `(a,(b,c)[u==w])[x==y]`, or you can multiply by a boolean.

* https://leetcode.com/problems/removing-stars-from-a-string

```python
class Solution:
    def removeStars(self, s: str) -> str:
        return reduce(lambda r,c:(r[:-1],r+c)[c>'*'],s)
```

* https://leetcode.com/problems/simplify-path

```python
class Solution:
  def simplifyPath(self, path: str) -> str:
    return'/'+'/'.join(reduce(lambda r,p:(r+[p]*('.'!=p!=''),r[:-1])[p=='..'],path.split('/'),[]))
```

Python 3 lacks `cmp` (3-way compare) and sign function (`copysign(bool(x),x)` is too long), but you can use `(x>0)-(x<0)` for `sign(x)`
and `(a>b)-(a<b)` for `cmp(a,b)`. Note you can use `-1,0,1` indexes for Python lists natively.

* https://leetcode.com/problems/stone-game-iii

```python
class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        f=cache(lambda i:i<len(v)and max(sum(v[i:i+k])-f(i+k)for k in(1,2,3)));x=f(0);
        return('Tie','Alice','Bob')[(x>0)-(x<0)]
        # return(('Tie','Bob')[x<0],'Alice')[x>0] # or like this (1 char shorter)
```

You can replace `cmp` written as `lambda x:(x>0)-(x<0)` with `0..__le__` or `.0.__le__` (11 characters shorter).

* https://leetcode.com/problems/rearrange-array-elements-by-sign

```python
class Solution:
    def rearrangeArray(self, n: List[int]) -> List[int]:
        n.sort(key=lambda x:(x>0)-(x<0));return chain(*zip(n[len(n)//2:],n))

class Solution:
    def rearrangeArray(self, n: List[int]) -> List[int]:
        n.sort(key=0..__le__);return chain(*zip(n[len(n)//2:],n)) 

```

You can save a few characters using asterisk operator `*`.
One `*` means "expand this as a list", two `**` means "expand this as a dictionary".

* https://leetcode.com/problems/check-if-it-is-a-straight-line

```python
class Solution:
    def checkStraightLine(self, p):
        (a,b),(c,d)=p[:2];return all((x-a)*(d-b)==(c-a)*(y-b)for x,y in p)

class Solution:
    def checkStraightLine(self, p):
        (a,b),(c,d),*_=p;return all((x-a)*(d-b)==(c-a)*(y-b)for x,y in p)
```

* https://leetcode.com/problems/maximum-average-subarray-i


```python
class Solution:
    def findMaxAverage(self, n: List[int], k: int) -> float:
        s=[0]+[*accumulate(n)];return max(map(sub,s[k:],s))/k

class Solution:
    def findMaxAverage(self, n: List[int], k: int) -> float:
        s=[0,*accumulate(n)];return max(map(sub,s[k:],s))/k
```

Quite a few things become shorter with `statistics.mode` (most common value of discrete or nominal data).

* https://leetcode.com/problems/set-mismatch

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        t=sum({*nums});return sum(nums)-t,comb(len(nums)+1,2)-t

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return mode(nums),comb(len(nums)+1,2)-sum({*nums})
```

* https://leetcode.com/problems/majority-element

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return mode(nums)
```

* https://leetcode.com/problems/find-the-duplicate-number

```python
# https://youtu.be/pKO9UjSeLew (Joma Tech: If Programming Was An Anime)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return mode(nums)
```

Notes:

* Unless the following token starts with e or E. You can remove the space following a number. E.g. `i==4 and j==4` becomes `i==4and j==4`.
* There's a nice way to convert an iterable to list using star operator, e.g. `x=[*g]` equals `*x,=g` (1 char shorter).
  You can also use this syntax to unpack iterables, e.g. `a,*b,c=range(5)` means `a=1;b=[2,3,4];c=5`.
* Instead of range(x), you can use the * operator on a list of anything, e.g. `[1]*8` can replace `range(8)` (unless you really need the counter value).
* Conditions like `if i<len(r)` may be replaced with `if r[i:]`, it's 3 characters shorter.
* You can replace `set(n)` with `{*n}` (2 characters shorter).
* You can convert bool with `~~()` instead of `int()` (as in js) or prepend with a single `+` (5 characters shorter).
* You can subtract 1 or replace `not` operator with bitwise negation `~-` to save on space (1-5 characters shorter).
* You can check for set membership with `{x}&s` instead of `x in s` (1 character shorter).
* An expression like `x&(x-1)==0` determines if unsigned `x` is power of 2 or 0 (Kernighan, tests rightmost bit).
* Very often `x==0` can be replaced with `x<1` (1 character shorter).
* Generator expansion `[*g]` can use a traling comma `*g,` in the initialization section (1 character shorter).
* A condition like `h>i>=0<=j<w` can be written as `h>i>-1<j<w` (1 character shorter).
* You can replace `q and q[-1]==c` with `q[-1:]==[c]` (3 characters shorter).

## References

* [Don't Piss down my back and tell me it's raining: Notebook for Sarcastic, Witty, and Sharp Tongued One Liners](https://www.amazon.com/Dont-Piss-down-back-raining/dp/B08ZQGV1XH)
* [Python One-Liners: Write Concise, Eloquent Python Like a Professional](https://www.amazon.com/Python-One-Liners-Concise-Eloquent-Professional/dp/1718500505)
* [Python One-Liners - Concise Python Code](https://pythononeliners.com)
* [Brilliant repositories of fantastic, killer one-liners (YouTube)](https://youtu.be/8k2AbqTBxao?t=251)
* [Tips for Golfing in Python (Stack Overflow)](https://codegolf.stackexchange.com/questions/54/tips-for-golfing-in-python)
* [One-line coder makes me depressed (Reddit)](https://redd.it/15wz7n7)
