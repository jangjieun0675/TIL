# 2024. 06. 05. 수요일
# 오늘의 학습 키워드 : Greedy(탐욕법)
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0  # 'L'과 'R'의 개수를 추적하기 위한 변수
        res = 0  # 균형 잡힌 문자열의 개수를 추적하기 위한 변수
        for char in s:  # 문자열 s의 각 문자에 대해 반복
            if char == 'L':  # 문자가 'L'인 경우
                count += 1  # count를 1 증가
            else:  # 문자가 'R'인 경우
                count -= 1  # count를 1 감소
            if count == 0:  # count가 0이면, 'L'과 'R'의 개수가 같으므로 균형 잡힌 문자열을 찾았음
                res += 1  # 결과 변수를 1 증가
        return res  # 균형 잡힌 문자열의 개수를 반환

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.


# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".