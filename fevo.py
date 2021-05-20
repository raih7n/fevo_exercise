# Input: "aabbbccda"

def process_input(input: str):
    
    if not input:
        return ""

    current_character = None
    previous_character = input[0]
    count_per_character = 0
    
    result_string = ""

    for char in input:
        current_character = char
        if char != previous_character:
            result_string += previous_character
            result_string += str(count_per_character)
            count_per_character = 0

        previous_character = char     
        count_per_character += 1

    result_string += previous_character
    result_string += str(count_per_character)

    print(result_string)

process_input("a2b3b3b4c2")


        


