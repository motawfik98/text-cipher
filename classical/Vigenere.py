import read_from_file


def generate_key(key, plain_text, mode):
    generated_key = ""
    key_length = len(key)
    plain_text_length = len(plain_text)

    loops = (plain_text_length // key_length) + 1
    if mode:
        generated_key = key + plain_text
    else:
        for i in range(loops):
            generated_key += key

    if len(generated_key) > plain_text_length:
        return generated_key[0: plain_text_length]
    return generated_key


def encrypt(key, plain_text, mode):
    cipher_text = ""
    generated_key = generate_key(key, plain_text, mode)
    generated_key = generated_key.upper()
    plain_text = plain_text.upper()

    for i in range(len(generated_key)):
        cipher_text += chr(((ord(generated_key[i]) + ord(plain_text[i])) % 26) + ord('A'))
    return cipher_text


input_file = open("../Files/Vigenere/vigenere_plain.txt")
output_file = open("../Files/Vigenere/vigenere_output_auto.txt", "w")

text = read_from_file.read_message(input_file)
key = input("Enter your key: ")
mode = bool(input("Enter mode (0 for auto & anything else for repeating): "))
output_file.write(encrypt(key, text, mode))

input_file.close()
output_file.close()
