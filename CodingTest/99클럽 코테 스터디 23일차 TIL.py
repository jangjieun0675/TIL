# 2024. 06. 12. 수요일
# 오늘의 학습 키워드 : 그래프
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 첫 번째 엣지와 두 번째 엣지를 확인
        # 별 그래프에서 중심 노드는 모든 엣지에 포함되므로, 첫 번째 엣지와 두 번째 엣지에 공통으로 포함된 노드가 중심 노드
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]  # 첫 번째 노드가 중심 노드인 경우
        else:
            return edges[0][1]  # 두 번째 노드가 중심 노드인 경우


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# There is an undirected star graph consisting of n nodes labeled from 1 to n.
#  A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 
# Return the center of the given star graph.