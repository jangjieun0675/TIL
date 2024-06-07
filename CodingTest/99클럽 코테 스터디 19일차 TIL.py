# 2024. 06. 07. 금요일
# 오늘의 학습 키워드 : 동적계획법
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            triangle = [[1], [1, 1]]
            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
                row.append(1)
                triangle.append(row)
            return triangle

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1] * i for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]: