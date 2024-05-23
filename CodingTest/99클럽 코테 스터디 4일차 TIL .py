# 2024. 05. 23. 목요일
# 오늘의 학습 키워드 : 스택/큐
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table ={
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s :
            if char not in table: # 여는 괄호가 들어오면 스택에 추가
                stack.append(char)
            # 스택이 비어 있으면 여는 괄호가 없는 것이므로 false
            # 닫는 괄호가 들어왔을 때 스택에 pop된 원소와 매칭되지 않으면 false
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항
# 오늘 문제는 풀지 못했다...
# 스택을 사용하는 문제하는 것을 인지했으나 모든 입력을 스택으로 추가해야한다고만 생각했지
# 여는 괄호만 스택에 추가한다는 생각을 못했다.
# 천천리 복기하면서 스택/큐와 익숙해져보자!!

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.