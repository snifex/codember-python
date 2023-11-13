
def main():
    #You can implement a function that read from a file the line
    #Like this problem it's using only a single line, for practicity
    #i pasted as a hard-coded
    input_chars = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"
    list_input = [i for i in input_chars]
    
    counter = 0

    # Make a dict simulating a switch case
    dict_cases = {
        '#': 'increase',
        '@': 'decrease',
        '*': 'multiply',
        '&': 'print' 
    }

    for letter in list_input:
        case = dict_cases[letter]
        if case == 'increase':
            counter += 1
        elif case == 'decrease':
            counter -= 1
        elif case == 'multiply':
            counter *= counter
        elif case == 'print':
            print(counter, end="")


if __name__ == '__main__':
    main()