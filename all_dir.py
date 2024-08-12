import os

def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        for item in os.listdir(path):
            print(item)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
directory_path = '/MySQL'  # Current directory
print_directory_contents(directory_path)
 