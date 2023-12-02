def read_lines(filename: str):
    """
    Read the txt file returning each line of the file in a lazy mode

        Parameters
            filename (str): The filename with the text to read

        Returns
            lines (list): A List with each line of the txt
    """
    with open(f"./assets/{filename}", 'r', encoding="UTF-8") as txt_file:
        for line in txt_file:
            yield line

def write_archive(name_archive: str, lista:list) -> None:
    """Write an archive with a tuple

    Args:
        name_archive (str): Name of the result archive
        lista (list): List to write
    """
    with open(f"./results/{name_archive}.txt", "w", encoding="utf-8") as output_file:
        text_formatted = (f"{i}\n" for i in lista)
        output_file.writelines(text_formatted)

def find_duplicates(str_2_remove: str) -> str:
    """Find duplicates in a string that

    Args:
        str_2_remove (str): String to remove duplicates from

    Returns:
        str: Returns the strings that repeats in the string passed
    """
    x = filter(lambda x: str_2_remove.count(x) >= 2, str_2_remove)
    return ''.join(set(x))

def main():
    result = find_checksum()
    write_archive("checksums",result)

def find_checksum(number_password: int = 0) -> list:
    """Get the password of the given number list, if the number is not provided return the first one

    Args:
        number_password (int, optional): Number in the list that we want password. Defaults to 0.

    Returns:
        list
    """
    result_list = []
    # Get each line of the txt file 
    for line in read_lines("files_quarantine.txt"):
        #Split from each line the checksum and the string to check
        str_file , checksum = line.strip().split("-")

        # remove the duplicates from the str_file
        chars_duplicates = find_duplicates(str_file)
        real_checksum = str_file.replace(chars_duplicates, "")
        
        #Check the checksum against the real checksum
        if checksum == real_checksum:
            result_list.append(checksum)
            
    return result_list
        
        
    
if __name__ == '__main__':
    main()