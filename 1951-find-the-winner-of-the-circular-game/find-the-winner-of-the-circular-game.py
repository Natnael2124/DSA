class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1,n+1))

        start_idx = 0

        while len(players) > 1:
            remov_idx = (start_idx + k -1 ) % len(players)

            players.pop(remov_idx)

            start_idx = remov_idx

        return players[0]
        

                
                