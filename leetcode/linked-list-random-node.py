from lc import *

# type conversion for lambdas
def init(head: ListNode):
    pass

# TODO (write sampler)
def check(res, exp, *arg):
    return True

# reservoir sampling

class Solution:
    def __init__(self, head: ListNode):
        self.head = head
    def getRandom(self) -> int:
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k/n:
                ans = ans.next
                k += 1
        return ans.val

class Solution:
    def __init__(self, head: ListNode):
        self.head = head
    def getRandom(self) -> int:
        r,c,n = self.head.val,self.head.next,1
        while c:
            r,c,n = c.val if random.randint(1, n+1)==1 else r,c.next,n+1
        return r

# expand list

class Solution:
    def __init__(self, head: ListNode):
        self.v = (f:=lambda x:x and [x.val]+f(x.next) or [])(head)
    def getRandom(self) -> int:
        return random.choice(self.v)

Solution=type('',(),{'__init__':lambda s,h:setattr(s,'v',(f:=lambda x:x and [x.val]+f(x.next) or [])(h)),'getRandom':lambda s:random.choice(s.v)})

test('''
382. Linked List Random Node
Medium

1975

473

Add to List

Share
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
 

Example 1:


Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 

Constraints:

The number of nodes in the linked list will be in the range [1, 104].
-10^4 <= Node.val <= 10^4
At most 10^4 calls will be made to getRandom.
 

Follow up:

What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?

Accepted
165,198
Submissions
276,676

''',init=init,check=check,classname=Solution
)

