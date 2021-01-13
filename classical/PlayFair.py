import numpy as np
from string import ascii_uppercase


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def read_message():
    lines = input_file.readlines()
    joined_lines = "".join(lines)
    formatted_message = ""
    for character in joined_lines:
        if character == "\n" or character == " ":
            continue
        formatted_message += character
    return formatted_message.upper()


def construct_matrix(key):
    key = key.upper()
    result = np.array([], dtype=str)
    for character in key:
        if character not in result:
            if character == 'I':
                if 'J' not in result:
                    result = np.append(result, 'J')
            else:
                result = np.append(result, character)
    for capital_letter in ascii_uppercase:
        if capital_letter not in result:
            if capital_letter == 'I':
                if 'J' not in result:
                    result = np.append(result, 'J')
            else:
                result = np.append(result, capital_letter)
    return result


def clean_input(input_msg):
    clean = ""
    for i in range(len(input_msg) - 1):
        clean += input_msg[i]
        if input_msg[i] == input_msg[i + 1]:
            clean += 'X'
    clean += input_msg[-1]
    if len(clean) & 1:
        clean += "X"
    return clean


def encode(msg_to_process, matrix):
    cipher_text = ""
    for char1, char2 in pairwise(msg_to_process):
        if char1 == 'I':
            char1 = 'J'
        if char2 == 'I':
            char2 = 'J'
        row1, col1 = divmod(matrix.index(char1), 5)
        row2, col2 = divmod(matrix.index(char2), 5)

        if row1 == row2:
            cipher_text += matrix[row1 * 5 + (col1 - 1) % 5]
            cipher_text += matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[((row1 - 1) % 5) * 5 + col1]
            cipher_text += matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            cipher_text += matrix[row1 * 5 + col2]
            cipher_text += matrix[row2 * 5 + col1]
    return cipher_text


input_file = open("../Files/PlayFair/playfair_plain.txt")
output_file = open("../Files/PlayFair/playfair_output.txt", "w")

play_fair_matrix = np.zeros((5, 5), dtype=str)
message = read_message()
cleaned_input = clean_input(message)
key = input("Enter your key: ")
matrix = construct_matrix(key)
output = encode(cleaned_input, matrix.tolist())
output_file.write(output)

input_file.close()
output_file.close()
