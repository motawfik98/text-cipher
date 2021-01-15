def read_message(input_file):
    lines = input_file.readlines()
    joined_lines = "".join(lines)
    formatted_message = ""
    for character in joined_lines:
        if character == "\n" or character == " ":
            continue
        formatted_message += character
    return formatted_message


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)
