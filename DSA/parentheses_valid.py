class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        moves = 0
        for i in s:
            if i == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                moves += 1
                balance = 0
        moves += balance
        return moves