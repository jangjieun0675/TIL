# 2024. 06. 28. 금요일
# 오늘의 학습 키워드 : Greedy
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # '1'의 개수를 셈
        ones_count = s.count('1')
        # '0'의 개수를 셈
        zeros_count = len(s) - ones_count
        
        # 가장 큰 홀수 이진수를 만듦
        result = '1' * (ones_count - 1) + '0' * zeros_count + '1'
        
        return result

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be created from the given combination.

# Note that the resulting string can have leading zeros.


# Example 1:

# Input: s = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
# Example 2:

# Input: s = "0101"
# Output: "1001"
# Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".