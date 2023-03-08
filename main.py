# Aditya Khera

# menu
def print_menu():
    print()
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    print("Please enter an option:", end=' ')


# encodes password by string conversion, adding 3 for each digit and concatenating after through print statements
def encode(password):
    output = 0
    str_output = ''
    for digit in str(password):
        if digit.isdigit():
            output = int(digit) + 3

            # # if the value ends up higher than 9, reduce the value by 10
            # so it stays a single digit
            if output > 9:
                output -= 10

            str_output += str(output)
    print('Your password has been encoded and stored!')
    return str_output


# decodes the password by subtracting 3 from each value, returning the decoded password
def decode(encoded_password):
    decoded_password = ''

    for index in range(0, len(encoded_password)):
        decoded_value = int(encoded_password[index]) - 3

        # if the value becomes negative, add 10 to the value to keep it positive
        if decoded_value < 0:
            decoded_value += 10

        decoded_password += str(decoded_value)

    return decoded_password


# loops the application menu until the user exits
if __name__ == "__main__":
    encoded_password = ''

    while True:
        print_menu()
        option = int(input())
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
        elif option == 2:
            decoded_password = decode(encoded_password)
            print("The encoded password is ", encoded_password, ", and the original password is ", decoded_password, sep='')
        elif option == 3:
            break
