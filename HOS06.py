# This code demonstrates file handling in Python using the pathlib module. 
# It includes functions to read or create a file, read a file line by line, rename a file, and delete a file, 
# with appropriate exception handling for each operation

from pathlib import Path
def read_or_create_file(file_path):# Function to read a file or create it if it does not exist
    try:
        contents = file_path.read_text()# Read the contents of the file
        print(contents)

    except FileNotFoundError:# Handle the case where the file does not exist
        print(f"The file at {file_path} was not found. Creating a new file.")
        file_path.touch() # Creates an empty file


#read_or_create_file(Path("example.txt")) 
# Example usage of the function to read or create a file
def read_file_line_by_line(file_path):#
    try:
        lines = file_path. read_text().splitlines()
        for line_number, line_content in enumerate(lines, 1):
            print(f"{line_number}: {line_content.strip()}")
    except FileNotFoundError:# Handle the case where the file does not exist
        print(f"The file at {file_path} was not found.")

# Function to rename a file and handle exceptions if the file does not exist or other errors occur
def rename_file(current_path, new_path):
    try:
        current_path. rename(new_path)# Rename the file from current_path to new_path
        print(f"File renamed to {new_path}")
    except FileNotFoundError:# Handle the case where the file does not exist
        print(f"The file {current_path} does not exist.")
    except Exception as e:# Handle other exceptions that may occur during the renaming process
        print(f"Error: {e}")

#delete_file function to delete a file and handle exceptions if the file does not exist or other errors occur
def delete_file(file_path):
    try:
        file_path.unlink()
        print(f"File {file_path} has been deleted.")
    except FileNotFoundError:# Handle the case where the file does not exist
        print(f"The file {file_path} does not exist.")
    except Exception as e:# Handle other exceptions that may occur during the deletion process
        print(f"Error: {e}")

# Main function to demonstrate the usage of the above functions
def main():
    file_path = Path('example.txt')
    read_or_create_file(file_path)# Read or create the file

    print("Original file content:")
    read_file_line_by_line(file_path)# Read the file line by line

    new_file_path = Path('renamed_example.txt')
    rename_file(file_path, new_file_path)# Rename the file

    print("\nRenamed file content:")
    read_file_line_by_line(new_file_path)# Read the renamed file line by line

    if input(f"Do you want to delete the file {new_file_path}? (y/n) ") == 'y':
        delete_file(new_file_path)# Delete the file if the user confirms

if __name__ == "__main__":
    main()# Call the main function to execute the file operations