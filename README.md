# python-week5

# Python File Handling Assignment

## Overview

This Python project demonstrates the fundamental concepts of file handling, including file creation, reading, appending, and error handling. The project is structured to meet the requirements of Week 5 of the assignment, showcasing the following tasks:

- **File Creation**: Creating a text file and writing initial content.
- **File Reading**: Reading the content of the file and displaying it on the console.
- **File Appending**: Appending additional content to the existing file without overwriting the original content.
- **Error Handling**: Implementing error handling mechanisms to catch and manage file-related exceptions.

## Files

- **file_handling_assignment.py**: The main Python script that performs all the tasks.
- **my_file.txt**: The text file created and modified by the script.

## Tasks and Features

### 1. File Creation and Writing
- The script creates a text file named `my_file.txt` in write mode.
- Three lines of text are written to the file, including a mix of strings and numbers.

### 2. File Reading and Displaying Content
- The script reads the contents of `my_file.txt` and prints them to the console.
- This is achieved using Python's file handling capabilities with the `read()` method.

### 3. File Appending
- The script reopens `my_file.txt` in append mode and adds three more lines of text.
- The original content remains intact, and the additional lines are appended at the end of the file.

### 4. Error Handling
- The script includes error handling with `try`, `except`, and `finally` blocks to handle potential issues such as `FileNotFoundError` and `PermissionError`.
- A final message is displayed to indicate the completion of the file handling tasks, whether or not an error occurred.

## How to Run

1. Clone the repository or download the script files to your local machine.
2. Run the Python script using the following command:
    ```bash
    python file.py
    ```
3. Observe the output in the console, which will show:
   - The result of creating and writing to the file.
   - The file content displayed after reading.
   - The updated file content after appending new lines.

## Error Handling Demonstration

The script is designed to handle errors that may occur during file operations, including:
- **FileNotFoundError**: Triggered if the file is not found during reading or appending.
- **PermissionError**: Triggered if there are permission issues accessing the file.
- **General Errors**: Handled by catching any other exceptions and displaying appropriate messages.


