# Function to read, modify, and write file content
def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File content has been modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading or writing to the file.")
    

# Function to ask the user for a filename and handle errors
def handle_file_errors():
    input_filename = input("Please enter the filename you want to read: ")
    output_filename = input("Please enter the output filename to write to: ")

    read_and_modify_file(input_filename, output_filename)


# Run the program
handle_file_errors()
