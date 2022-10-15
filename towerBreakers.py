# Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.The rules of the game are as follows:

# Initially there are  towers.
# Each tower is of height .
# The players move in alternating turns.
# In each turn, a player can choose a tower of height  and reduce its height to , where  and  evenly divides .
# If the current player is unable to make a move, they lose the game.
# Given the values of  and , determine which player will win. If the first player wins, return . Otherwise, return .

# Example.
n = 2
m = 2

# There are 2 towers, each 6 units tall. Player 1 has a choice of two moves:
# - remove 3 pieces from a tower to leave 3 as 6 modulo 3 = 0
# - remove 5 pieces to 1 leave 

# Let Player 1 remove 3. Now the towers are 3 and 6 units tall.

# Player 2 matches the move. Now the towers are both 3 units tall.

# Now Player 1 has only one move.

# Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall.
# Player 2 matches again. Towers are both 1 unit tall.

# Player 1 has no move and loses. Return 2.


def towerBreakers(n, m):
    return 2 if m == 1 or n % 2 == 0 else 1


print(towerBreakers(n, m))

#  n == 1: p1 wins
#  m == 1: p2 wins
#  n == odd: p1 wins
#  n == even: p2 wins