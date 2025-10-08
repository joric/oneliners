from lc import *

# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/solutions/3367968/python-1-line-code-beats-98-7/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        return (lambda p:[len(p)-bisect_left(p,(success+a-1)//a) for a in spells])(sorted(potions))

class Solution:
    def successfulPairs(self, s: List[int], p: List[int], c: int) -> List[int]:
        p.sort();return[len(p)-bisect_left(p,(c+a-1)//a)for a in s]

class Solution:
    def successfulPairs(self, s: List[int], p: List[int], c: int) -> List[int]:
        p.sort();return[len(p)-bisect_left(p,c/a)for a in s]

test('''
2300. Successful Pairs of Spells and Potions
Medium

595

18

Add to List

Share
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
 

Constraints:

n == spells.length
m == potions.length
1 <= n, m <= 10^5
1 <= spells[i], potions[i] <= 10^5
1 <= success <= 10^10

Accepted
26,963
Submissions
77,294
Seen this question in a real interview before?

Yes

No
Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.
Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.
We can efficiently do this by sorting the potions based on strength and using binary search.
''')
