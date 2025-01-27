# 2024. 05. 29. 수요일
# 오늘의 학습 키워드 : 완전탐색
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            scores[2] += 1

    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx+1)

    return result

    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항
# def solution(answers):
    # n1, n2, n3 = 0, 0, 0
    # a1 = [1,2,3,4,5]
    # a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # for i in range(len(answers)):
    #     if a1[i] == answers[i]:
    #         n1 += 1
    #     if a2[i] == answers[i]:
    #         n2 += 1
    #     if a3[i] == answers[i]:
    #         n3 += 1

    # # 변수들을 리스트로 만들기
    # nums = [n1, n2, n3]

    # # 가장 큰 값 찾기
    # max_val = max(nums)

    # # 가장 큰 값의 인덱스(들) 찾기
    # max_indices = [i+1 for i, n in enumerate(nums) if n == max_val]

    # return max_indices

# 사용자의 코드에는 중요한 부분에서 오류가 있었다. 
# 특히, a1, a2, a3 배열에 대한 인덱스 접근 방식에 문제이다.
# 각 수포자가 찍는 방식의 길이에 따라 인덱스를 순환시켜야 한다. 
# 현재 코드에서는 if 문 안에서 a1[i], a2[i], a3[i]를 바로 비교하고 있으나, 
# 이는 각 배열의 길이를 넘어서는 인덱스에 대한 처리가 없기 때문에 오류가 발생할 수 있다. 
# 각 수포자 배열의 길이로 인덱스 i를 나눈 나머지를 사용하여 각각의 배열에 접근해야 한다. 
# 즉, a1[i % len(a1)], a2[i % len(a2)], a3[i % len(a3)]와 같은 방식으로 수정해주어야 한다. 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]
# 입출력 예 설명
# 입출력 예 #1

# 수포자 1은 모든 문제를 맞혔습니다.
# 수포자 2는 모든 문제를 틀렸습니다.
# 수포자 3은 모든 문제를 틀렸습니다.
# 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

# 입출력 예 #2

# 모든 사람이 2문제씩을 맞췄습니다.