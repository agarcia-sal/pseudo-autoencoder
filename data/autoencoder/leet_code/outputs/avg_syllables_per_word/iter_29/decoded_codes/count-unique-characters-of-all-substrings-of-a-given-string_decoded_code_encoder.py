class Solution:  
    def uniqueLetterString(self, s: str) -> int:  
        MODULO = 10**9 + 7  
        length_of_s = len(s)  

        last_positions = [-1] * 26  
        last_positions_two = [-1] * 26  

        total_result = 0  

        for index, character in enumerate(s):  
            character_index = ord(character) - ord('A')  

            total_result += (index - last_positions[character_index]) * (last_positions[character_index] - last_positions_two[character_index])  
            total_result %= MODULO  

            last_positions_two[character_index] = last_positions[character_index]  
            last_positions[character_index] = index  

        for index in range(26):  
            total_result += (length_of_s - last_positions[index]) * (last_positions[index] - last_positions_two[index])  
            total_result %= MODULO  

        return total_result