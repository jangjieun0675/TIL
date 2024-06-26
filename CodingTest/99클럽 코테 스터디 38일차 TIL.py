# 2024. 06. 26. 수요일
# 오늘의 학습 키워드 : Heap
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0  # 정답을 저장할 변수 초기화
        
        # 모든 행이 비어있지 않은 동안 반복
        while grid and grid[0]:
            max_deleted_values = []  # 각 행에서 삭제된 최대값을 저장할 리스트
            for row in grid:
                max_value = max(row)  # 현재 행에서 최대값 찾기
                max_deleted_values.append(max_value)  # 최대값을 리스트에 추가
                row.remove(max_value)  # 최대값을 행에서 제거
            
            # 현재 반복에서 삭제된 최대값들 중에서 가장 큰 값을 정답에 더하기
            answer += max(max_deleted_values)
        
        return answer  # 최종 정답 반환

        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# You are given an m x n matrix grid consisting of positive integers.

# Perform the following operation until grid becomes empty:

# Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.

# Return the answer after performing the operations described above.

# Example 1:


# Input: grid = [[1,2,4],[3,3,1]]
# Output: 8
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
# - In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
# - In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
# The final answer = 4 + 3 + 1 = 8.
# Example 2:


# Input: grid = [[10]]
# Output: 10
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 10 from the first row. We add 10 to the answer.
# The final answer = 10.