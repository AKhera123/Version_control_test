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
def encode_password(password):
    output = 0
    str_output = ''
    for digit in str(password):
        if digit.isdigit():
            output = int(digit) + 3
            str_output += str(output)
    return str_output


if __name__ == "__main__":
    while True:
        print_menu()
        option = int(input())
        if option == 1:
            password = input("Please enter your password to encode: ")
            print(encode_password(password))
        elif option == 2:
            print("The encoded password is ", encode_password(password), ", and the original password is ", password, sep='')
        elif option == 3:
            break
