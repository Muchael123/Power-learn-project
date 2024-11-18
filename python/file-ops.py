# 1. Define a function to read from a file
def read_file(input_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            # Read the contents of the file
            content = file.read()
        # Return the content
        return content
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return None
    except IOError:
        print(f"Error: An error occurred while reading the file.")
        return None

# 2. Define a function to modify the content
def modify_content(content):
    if content is None:
        return None
    # Apply modification to content (e.g., convert to uppercase, add text)
    modified_content = content.upper()  # Example modification (convert to uppercase)
    return modified_content

# 3. Define a function to write to a new file
def write_file(output_filename, modified_content):
    if modified_content is None:
        print("Error: No content to write to the file.")
        return
    try:
        # Open the output file in write mode
        with open(output_filename, 'w') as file:
            # Write the modified content to the new file
            file.write(modified_content)
        print(f"File content has been modified and saved to '{output_filename}'.")
    except IOError:
        print(f"Error: An error occurred while writing to the file.")

# 4. Call the functions in sequence
def process_files():
    input_filename = input("Please enter the filename you want to read: ")
    output_filename = input("Please enter the output filename to write to: ")

    # Read the original file's contents
    content = read_file(input_filename)

    # If content is successfully read, modify the content
    if content is not None:
        modified_content = modify_content(content)

        # Write the modified content to the new file
        write_file(output_filename, modified_content)

# 5. Run the process
process_files()
