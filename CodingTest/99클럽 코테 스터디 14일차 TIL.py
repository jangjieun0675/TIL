# 2024. 06. 02. 일요일
# 오늘의 학습 키워드 : 깊이/너비 우선 탐색
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # Swap the left and right child nodes
            root.left, root.right = root.right, root.left
            
            # Recursively invert the left and right subtrees
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# Given the root of a binary tree, invert the tree, and return its root.
# Example 1:

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []