# file_handling_assignment.py

# Task 1: File Creation and Writing to File
try:
    # Open "my_file.txt" in write mode
    with open("my_file.txt", 'w') as file:
        # Writing three lines to the file
        file.write("This is line 1.\n")
        file.write("The number is 42.\n")
        file.write("Python file handling demo.\n")
    print("File created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred while creating or writing to the file: {e}")

# Task 2: File Reading and Displaying Content
try:
    # Open "my_file.txt" in read mode
    with open("my_file.txt", 'r') as file:
        # Reading and displaying the content
        content = file.read()
        print("\nContent of 'my_file.txt':")
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Task 3: File Appending
try:
    # Open "my_file.txt" in append mode
    with open("my_file.txt", 'a') as file:
        # Appending three additional lines
        file.write("This is an appended line 1.\n")
        file.write("Another number is 99.\n")
        file.write("File handling assignment continued.\n")
    print("\nAdditional content appended successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Task 4: Reading Updated Content with Error Handling
try:
    # Reopen the file in read mode to display updated content
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("\nUpdated content of 'my_file.txt':")
        print(updated_content)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling demonstration completed.")
