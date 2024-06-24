# 2024. 06. 24. 월요일
# 오늘의 학습 키워드 : 스택/큐
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # 가격의 인덱스를 추적하기 위한 스택을 초기화
        for i, price in enumerate(prices):  # 가격 목록을 순회
            # 스택이 비어있지 않고, 현재 가격이 스택의 맨 위 인덱스의 가격보다 작거나 같은 동안
            while stack and prices[stack[-1]] >= price:
                # 스택의 맨 위 인덱스의 가격에서 현재 가격을 뺀다
                prices[stack.pop()] -= price
            stack.append(i)  # 현재 인덱스를 스택에 추가
        return prices  # 할인이 적용된 가격 목록을 반환

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.


# Example 1:

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.
# Example 3:

# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]