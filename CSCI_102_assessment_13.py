# Jackson Krieger
# CSCI 102
# Assessment 13
# References: Went to office hours
# Time:


if __name__ == "__main__":
    print(
        "Welcome to our Caesar Cipher Algorithm!\n" +
        "Choose one of the following methods:\n" +
        "\t1 - Encryption\n" +
        "\t2 - Decryption"
    )
    while True:
        userIn = str(input("OPERATION> "))
        # If the user inputs 1, for encryption
        if userIn == "1":
            # TODO: use your encryption function here
            break
        # If the user inputs 2, for encryption
        elif userIn == "2":
            plain_text = ''
            cipher_text = input('MESSAGE TO DECRYPT> ')
            for i in range(26):
        # Decrypt the cipher text by shifting the letters by i positions.
                for ch in cipher_text:
                    if ch.isalpha():
                        shift = ord(ch) + i
                        if ch.isupper():
                            if shift > ord('Z'):
                                shift -= 26
                            elif shift < ord('A'):
                                shift += 26
                        else:
                            if shift > ord('z'):
                                shift -= 26
                            elif shift < ord('a'):
                                shift += 26
                        plain_text += chr(shift)
                    else:
                        plain_text += ch

# Print the decrypted text and the shift used.
                print(f"Shift: {26-i}: {plain_text}")
                plain_text = ""
            break
        else:
            print("Invalid Operation!")
