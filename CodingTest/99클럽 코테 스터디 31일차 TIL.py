# 2024. 06. 19. 수요일
# 오늘의 학습 키워드 : 문자열
# 해시태그 : #99클럽 #코딩테스트 준비 #개발자 취업 #항해99 #TIL

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 나의 문제 풀이
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Create a substitution table
        substitution_table = {}
        for char in key:
            if char not in substitution_table and char.isalpha():
                substitution_table[char] = chr(len(substitution_table) + ord('a'))

        # Decode the message
        decoded_message = ""
        for char in message:
            if char == ' ':
                decoded_message += ' '
            else:
                decoded_message += substitution_table[char]

        return decoded_message

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 개선할 사항


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 문제 설명
# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

 

# Example 1:


# Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# Output: "this is a secret"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".
# Example 2:


# Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# Output: "the five boxing wizards jump quickly"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".