# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("Line 1: This is the first line.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python is awesome!\n")
        print("File 'my_file.txt' created and written successfully.")
except Exception as e:
    print(f"Error occurred while creating and writing to the file: {e}")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("\nContents of 'my_file.txt':")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to access 'my_file.txt'.")
except Exception as e:
    print(f"Error occurred while reading the file: {e}")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Line 4: Appended line 1\n")
        file.write("Line 5: 987654\n")
        file.write("Line 6: Python is versatile!\n")
        print("\nAdditional lines appended to 'my_file.txt'.")
except Exception as e:
    print(f"Error occurred while appending to the file: {e}")
