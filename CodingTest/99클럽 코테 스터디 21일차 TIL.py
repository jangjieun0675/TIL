# 2024. 06. 09. 일요일
# 오늘의 학습 키워드 : 동적계획법
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def divisorGame(self, n: int) -> bool:
        # n+1 크기의 불리언 배열 dp를 초기화합니다. dp[i]는 칠판에 i가 있을 때 Alice가 이길 수 있으면 True, 그렇지 않으면 False입니다.
        dp = [False for _ in range(n+1)]
        
        # 각 숫자 i에 대해 2부터 n까지 반복합니다.
        for i in range(2, n+1):
            # 각 숫자 j에 대해 1부터 i//2 + 1까지 반복합니다.
            for j in range(1, i//2 + 1):
                # 만약 i가 j로 나누어 떨어지고, 칠판에 i - j가 있을 때 Alice가 이길 수 없다면,
                # 칠판에 i가 있을 때 Alice는 j를 선택하여 이길 수 있습니다.
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break  # 다른 j를 확인할 필요가 없으므로 반복문을 종료합니다.
        # 마지막으로, 칠판에 n이 있을 때 Alice가 이길 수 있는지 반환합니다.
        return dp[n]


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.

# Return true if and only if Alice wins the game, assuming both players play optimally.

# Example 1:

# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# Example 2:

# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.