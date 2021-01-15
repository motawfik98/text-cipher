import read_from_file


def extend_key(key, plain_text):
    generated_key = ""
    key_length = len(key)
    plain_text_length = len(plain_text)

    loops = (plain_text_length // key_length) + 1
    for i in range(loops):
        generated_key += key

    if len(generated_key) > plain_text_length:
        return generated_key[0: plain_text_length]
    return generated_key


def encrypt(plain_text, key):
    cipher_text = ""
    plain_text = plain_text.upper()
    key = key.upper()
    for i in range(len(plain_text)):
        cipher_text += chr((((ord(plain_text[i]) - ord('A')) ^ (ord(key[i]) - ord('A'))) % 26) + ord('A'))
    return cipher_text


input_file = open("../Files/Vernam/vernam_plain.txt")
output_file = open("../Files/Vernam/vernam_output.txt", "w")

text = read_from_file.read_message(input_file)
key = input("Enter your key: ")
key = extend_key(key, text)
output_file.write(encrypt(text, key))

input_file.close()
output_file.close()
