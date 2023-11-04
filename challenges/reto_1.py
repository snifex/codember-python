def read_txt(filename: str) -> list:
    """
    Read the txt file returning each line of the file

        Parameters
            filename (str): The filename with the text to read

        Returns
            lines (list): A List with each line of the txt
    """
    with open(filename, 'r', encoding="UTF-8") as txt_file:
        lines = [iterator.rstrip() for iterator in txt_file]
    return lines

def main():
    words_dict = {}
    str_result: str = ""

    for line in read_txt("codember.dev_data_message_01.txt"):
        for word in line.split(" "):
            if word in words_dict: 
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1

    # Create the final str using the key and value of the dict
    for key,value in words_dict.items():
        str_result += f"{key}{value}"

    print(str_result)


if __name__ == '__main__':
    main()