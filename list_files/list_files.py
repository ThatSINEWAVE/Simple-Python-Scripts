import os


def list_files(path="."):
    """Print all files and directories in the given folder"""
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except PermissionError:
        print(f"No permission to access '{path}'.")


if __name__ == "__main__":
    user_input = input("Enter folder path (leave empty for current directory): ").strip()

    if user_input == "":
        list_files()
    else:
        list_files(user_input)
