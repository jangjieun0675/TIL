# 2024. 06. 23. 일요일
# 오늘의 학습 키워드 : 스택/큐
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()  # 덱(deque) 초기화. 덱은 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조

    def ping(self, t: int) -> int:
        self.q.append(t)  # t를 덱의 오른쪽 끝에 추가
        while self.q[0] < t - 3000:  # 덱의 왼쪽 끝 요소가 t-3000보다 작으면,
            self.q.popleft()  # 왼쪽 끝 요소를 덱에서 제거
        return len(self.q)  # 덱의 길이, 즉 최근 3000 밀리초 동안의 요청 수를 반환

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3