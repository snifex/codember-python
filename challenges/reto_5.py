import csv
import re

def read_csv() -> list:
    """Read the CSV file and return each iteration a list of each line of the csv

    Returns:
        list: The csv file converted to a list
    """
    with open("./assets/database_attacked.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            yield row
        
def check_alphanumeric(str_2_check: str) -> bool:
    #Check if the str is not null
    if str_2_check == "":
        return False
    
    #Using regex check if the id is alphanumeric 
    pattern = re.compile("^[a-zA-Z0-9]+$")

    # Use the pattern to match the input string
    return bool(pattern.match(str_2_check))

def check_email(email_2_check: str) -> bool:
    #Check if the email is not null
    if email_2_check == "":
        return False
    
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    # Define the regex pattern for a simple email validation
    return bool(pattern.match(email_2_check))

def check_numerical(str_2_check: str) -> bool:
    # If the str it's null we return true
    if str_2_check == "":
        return True
    
    # Using regex check if the string given it's a number
    pattern = re.compile(r"^[0-9]+$")

    return bool(pattern.match(str_2_check))

def check_text(str_2_check: str) -> bool:
    # If the str it's null we return true
    if str_2_check == "":
        return True
    
    # Using regex check if the string given it's a text only string
    pattern = re.compile("^[a-zA-Z\s]+$")

    return bool(pattern.match(str_2_check))

def check_all_conditions(line_database: list) -> bool:
    return all(
        (check_alphanumeric(line_database[0]), #checks the id
        check_alphanumeric(line_database[1]), #check the username
        check_email(line_database[2]), #checks the email
        check_numerical(line_database[3]), #checks the age
        check_text(line_database[4])) #checks the coordinates
    )

def main():
    final_word : str = ""
    csv_list = read_csv()

    for line in csv_list:
        if not check_all_conditions(line):
            final_word += line[1][:1]

    print(final_word)


if __name__ == '__main__':
    main()

