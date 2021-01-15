import numpy as np
import read_from_file as file_input

input_file = None
output_file = None
matrix_size = 0

print("Select matrix size")
selection = int(input("Press (1) for 2x2 & (2) for 3x3: "))
if selection == 1:
    matrix_size = 4
    input_file = open("../Files/Hill/hill_plain_2x2.txt", "r")
    output_file = open("../Files/Hill/hill_output_2x2.txt", "w")
else:
    matrix_size = 9
    input_file = open("../Files/Hill/hill_plain_3x3.txt", "r")
    output_file = open("../Files/Hill/hill_output_3x3.txt", "w")

key_arr = np.array([], dtype=int)
for i in range(matrix_size):
    key_arr = np.append(key_arr, int(input()))
if matrix_size == 4:
    key_arr = key_arr.reshape(2, 2)
elif matrix_size == 9:
    key_arr = key_arr.reshape(3, 3)
plain_text = file_input.read_message(input_file)
plain_text_order = [ord(character) for character in plain_text]
plain_text_order = np.array(plain_text_order)
cipher_text = np.array([])
if matrix_size == 4:
    for i in range(0, len(plain_text_order), 2):
        offset1 = ord('A') if plain_text[i].isupper() else ord('a')
        offset2 = ord('A') if plain_text[i + 1].isupper() else ord('a')
        chars_to_encrypt = np.array([plain_text_order[i] - offset1, plain_text_order[i + 1] - offset2])
        multiplication = np.matmul(key_arr, chars_to_encrypt.reshape(2, 1))
        multiplication = np.remainder(multiplication, 26)
        multiplication[0] += offset1
        multiplication[1] += offset2
        cipher_text = np.append(cipher_text, multiplication)
else:
    for i in range(0, len(plain_text_order), 3):
        offset1 = ord('A') if plain_text[i].isupper() else ord('a')
        offset2 = ord('A') if plain_text[i + 1].isupper() else ord('a')
        offset3 = ord('A') if plain_text[i + 2].isupper() else ord('a')
        chars_to_encrypt = np.array([plain_text_order[i] - offset1, plain_text_order[i + 1] - offset2,
                                     plain_text_order[i + 2] - offset3])
        multiplication = np.matmul(key_arr, chars_to_encrypt.reshape(3, 1))
        multiplication = np.remainder(multiplication, 26)
        multiplication[0] += offset1
        multiplication[1] += offset2
        multiplication[2] += offset3
        cipher_text = np.append(cipher_text, multiplication)

cipher_text_chars = [chr(int(x)) for x in cipher_text]
cipher_text_str = "".join(cipher_text_chars)
output_file.write(cipher_text_str)

input_file.close()
output_file.close()
