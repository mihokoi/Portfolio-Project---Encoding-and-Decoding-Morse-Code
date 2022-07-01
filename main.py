# Python program to implement Morse Code encoding/decoding



MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '0': '----'}


# Encode
def encode(message_to_encode: str):
    result = ""
    for letter in message_to_encode:
        result += MORSE_CODE_DICT.get(letter.upper())
        result += " "
    return result


# Decode
def decode(message_to_decode: str):
    result = ""
    list_chars = message_to_decode.split(" ")
    for string in list_chars:
        for letter, morse_ in MORSE_CODE_DICT.items():
            if morse_ == string:
                result += letter
    return result

# Main function
def main():
    print("This program allows you to either encode or decode a message from/to Morse Code")

    while True:
        action = input("Decode: 'd', Encode: 'e': ")
        text = input("Type your message: ")
        if action.lower() == 'e' and action.isascii():
            print(encode(text))
        elif action.lower() == 'd' and action.isascii():
            print(decode(text))
        else:
            print("There was a problem parsing the action or the entered message wasn't a literal.")
        should_continue = input("Do you want to try again? (y/n) ")
        if should_continue.lower() == 'y' and should_continue.isascii():
            continue
        elif should_continue.lower() == 'n' and should_continue.isascii():
            break
        else:
            print("There was a problem checking how should we proceed. Probably the entered prompt wasn't a literal")
            break

    print("Goodbye!")


if __name__ == '__main__':
    main()




