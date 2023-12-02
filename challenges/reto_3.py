import re

def read_lines(filename: str):
    """
    Read the txt file returning each line of the file in a lazy mode

        Parameters
            filename (str): The filename with the text to read

        Returns
            lines (list): A List with each line of the txt
    """
    with open(filename, 'r', encoding="UTF-8") as txt_file:
        for line in txt_file:
            yield line

# def write_archive(name_archive: str, lista:list) -> None:
#     """Write an archive with a tuple

#     Args:
#         name_archive (str): Name of the result archive
#         lista (list): List to write
#     """
#     with open(name_archive + ".txt", "w", encoding="utf-8") as output_file:
#         text_formatted = (f"{i}\n" for i in lista)
#         output_file.writelines(text_formatted)
    
def main():
    find_password()
    # write_archive("list_wrongs",result_list)
    
def find_password(number_password: int = 0) -> list:
    """Get the password of the given number list, if the number is not provided return the first one

    Args:
        number_password (int, optional): Number in the list that we want password. Defaults to 0.

    Returns:
        list
    """
    
    result_list = []
    # Get each line of the txt file 
    for line in read_lines("encryption_policies.txt"):
        #Get the letter of the encryption of this line
        letter_line = line[line.find(":") - 1:line.find(":")]

        #Get the range
        range_letter:str = re.findall(r'\b\d+-\d+\b', line)[0]
        
        #Strip of the range_letter the numbers of the ranges
        minimum_count_letters = int(range_letter[:range_letter.find("-")])
        maximum_count_letters = int(range_letter[range_letter.find("-")+1:])

        #Convert in a range list to make a in 
        range_list = range(minimum_count_letters,maximum_count_letters)

        #Count the letters in the line and minus 1 because we don't want to count the letter to search 
        count_letters = line.count(letter_line) - 1
        
        if count_letters not in range_list:
            result_list.append(line)

    return result_list
        
    
if __name__ == '__main__':
    main()