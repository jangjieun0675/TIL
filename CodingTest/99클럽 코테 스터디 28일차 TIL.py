# 2024. 06. 16. 일요일
# 오늘의 학습 키워드 : 배열
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]ount


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# You are given a 0-indexed array of strings words and a character x.

# Return an array of indices representing the words that contain the character x.

# Note that the returned array may be in any order.


# Example 1:

# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
# Example 2:

# Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
# Output: [0,2]
# Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
# Example 3:

# Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
# Output: []
# Explanation: "z" does not occur in any of the words. Hence, we return an empty array.