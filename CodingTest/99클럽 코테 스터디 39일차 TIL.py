# 2024. 06. 27. 목요일
# 오늘의 학습 키워드 : Heap
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 각 행의 병사 수를 계산
        soldier_count = [(sum(row), i) for i, row in enumerate(mat)]
        
        # 병사 수와 행 인덱스를 기준으로 정렬
        sorted_rows = sorted(soldier_count)
        
        # 가장 약한 k개의 행의 인덱스를 추출
        weakest_rows = [index for _, index in sorted_rows[:k]]
        
        return weakest_rows

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.


# Example 1:

# Input: mat = 
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 
# k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 2 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 2 
# - Row 4: 5 
# The rows ordered from weakest to strongest are [2,0,3,1,4].
# Example 2:

# Input: mat = 
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]], 
# k = 2
# Output: [0,2]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 1 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 1 
# The rows ordered from weakest to strongest are [0,2,3,1].