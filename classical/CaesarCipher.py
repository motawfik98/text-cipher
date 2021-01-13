input_file = open("../Files/Caesar/caesar_plain.txt")
output_file = open("../Files/Caesar/caesar_output.txt", "w")

key = int(input("Enter key value: "))
for line in input_file:
    for character in line:
        if character.isalpha():
            # gets the offset to wrap the alphabetic characters
            offset = ord('A') if character.isupper() else ord('a')
            new_character = chr((ord(character) + key - offset) % 26 + offset)
            output_file.write(new_character)
    output_file.write("\n")

input_file.close()
output_file.close()
