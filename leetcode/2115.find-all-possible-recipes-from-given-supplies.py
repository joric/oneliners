from lc import *

# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/solutions/6561272/python3-simple-loops-with-set-operation-6-lines-only-beat-95/?envType=daily-question&envId=2025-03-21

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        curr = set(supplies)
        for r in recipes:
            for i, arr in enumerate(ingredients):
                if all(v in curr for v in arr):
                    curr.add(recipes[i])
        return list(curr - set(supplies))

class Solution:
    def findAllRecipes(self, r: List[str], g: List[List[str]], s: List[str]) -> List[str]:
        c={*s};[c.add(r[i])for _ in r for i,a in enumerate(g)if{*a}<=c];return[*(c-{*s})]

test('''
2115. Find All Possible Recipes from Given Supplies
Medium
Topics
Companies
Hint
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

Other solutions:

Input: recipes = ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"], ingredients = [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]], supplies = ["wi","otr","wbjr","fzr","xgp"]
Output: ["xevvq","izcad","bxgnm","i","hjvu","tokfq","z","g","b","hthy"]

Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
114.8K
Submissions
223.6K
Acceptance Rate
51.3%
Topics
Array
Hash Table
String
Graph
Topological Sort
Companies
Hint 1
Can we use a data structure to quickly query whether we have a certain ingredient?
Hint 2
Once we verify that we can make a recipe, we can add it to our ingredient data structure. We can then check if we can make more recipes as a result of this.
Similar Questions
Course Schedule II
Medium
Count Good Meals
Medium
''', sort=True)
