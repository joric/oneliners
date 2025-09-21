from lc import *

# https://leetcode.com/problems/design-movie-rental-system/solutions/1298452/ordered-sets/?envType=daily-question&envId=2025-09-21
# TODO

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]) -> None:
        self.prices = {}
        self.dropped = {}
        self.rented = SortedSet()
        for shop, movie, price in entries:
            if shop not in self.prices:
                self.prices[shop] = {}
            self.prices[shop][movie] = price
            if movie not in self.dropped:
                self.dropped[movie] = SortedSet()
            self.dropped[movie].add((price, shop))
    def search(self, movie: int) -> List[int]:
        if movie not in self.dropped:
            return []
        return [shop for price, shop in list(self.dropped[movie])[:5]]
    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[shop][movie]
        self.dropped[movie].remove((price, shop))
        self.rented.add((price, shop, movie))
    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[shop][movie]
        self.rented.remove((price, shop, movie))
        self.dropped[movie].add((price, shop))
    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in list(self.rented)[:5]]


# https://leetcode.com/problems/design-movie-rental-system/solutions/1298440/python-sortedlist-solution-explained/?envType=daily-question&envId=2025-09-21

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]) -> None:
        self.shops = defaultdict(SortedList)   #movie -> (price, shop)
        self.shop_movie = {}    #(shop, movie) -> price
        self.rented = SortedList()  # (price, shop, movie)
        for s, m, p in entries:
            self.shops[m].add((p, s))
            self.shop_movie[s, m] = p
    def search(self, movie: int) -> List[int]:
        return [y for _,y in self.shops[movie][:5]]
    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie[shop, movie]
        self.shops[movie].remove((price, shop))
        self.rented.add((price, shop, movie))
    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie[shop, movie]
        self.shops[movie].add((price, shop))
        self.rented.remove((price, shop, movie))
    def report(self) -> List[List[int]]:
        return [[y,z] for _,y,z in self.rented[:5]]

test('''
1912. Design Movie Rental System
Solved
Hard
Topics
premium lock icon
Companies
Hint
You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.

The system should support the following functions:

Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
Rent: Rents an unrented copy of a given movie from a given shop.
Drop: Drops off a previously rented copy of a given movie at a given shop.
Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.
Implement the MovieRentingSystem class:

MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
void rent(int shop, int movie) Rents the given movie from the given shop.
void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
List<List<Integer>> report() Returns a list of cheapest rented movies as described above.
Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.

 

Example 1:

Input
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
Output
[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]

Explanation
MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1);  // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report();   // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2);  // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.
 

Constraints:

1 <= n <= 3 * 105
1 <= entries.length <= 105
0 <= shopi < n
1 <= moviei, pricei <= 104
Each shop carries at most one copy of a movie moviei.
At most 105 calls in total will be made to search, rent, drop and report.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
8,987/24.8K
Acceptance Rate
36.2%
Topics
Array
Hash Table
Design
Heap (Priority Queue)
Ordered Set
Biweekly Contest 55
icon
Companies
Hint 1
You need to maintain a sorted list for each movie and a sorted list for rented movies
Hint 2
When renting a movie remove it from its movies sorted list and added it to the rented list and vice versa in the case of dropping a movie
''', MovieRentingSystem)
