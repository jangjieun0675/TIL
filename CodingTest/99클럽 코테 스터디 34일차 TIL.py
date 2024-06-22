# 2024. 06. 22. 토요일
# 오늘의 학습 키워드 : 스택/큐
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 학생들의 선호도를 큐로 변환합니다.
        students_queue = deque(students)
        # 샌드위치 종류를 스택으로 변환합니다.
        sandwiches_stack = deque(sandwiches)
        
        # 무한 루프를 시작합니다.
        while True:
            # 만약 큐의 맨 앞에 있는 학생이 스택의 맨 위 샌드위치를 선호한다면,
            if students_queue[0] == sandwiches_stack[0]:
                # 해당 학생은 샌드위치를 가져가고 큐에서 빠져나갑니다.
                students_queue.popleft()
                sandwiches_stack.popleft()
            else:
                # 그렇지 않다면, 해당 학생은 큐의 맨 뒤로 이동합니다.
                students_queue.rotate(-1)
            
            # 만약 모든 샌드위치가 다 떨어졌거나, 남은 학생들이 맨 위의 샌드위치를 원하지 않는다면 루프를 종료합니다.
            if len(sandwiches_stack) == 0 or students_queue.count(sandwiches_stack[0]) == 0:
                break
                
        # 더 이상 샌드위치를 먹지 못하는 학생들의 수를 반환합니다.
        return len(students_queue)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.


# Example 1:

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.
# Example 2:

# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3