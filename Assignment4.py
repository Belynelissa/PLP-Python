# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_and_modify_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Attempt to open and read the file
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify content (e.g., convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You don't have access to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
