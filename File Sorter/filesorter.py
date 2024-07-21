import os
import shutil
from pathlib import Path

def organize_files(directory):
    # Get a list of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for file in files:
        # Get the file extension
        ext = file.split('.')[-1] if '.' in file else 'no_extension'
        # Create a directory for the extension if it doesn't exist
        ext_dir = os.path.join(directory, ext)
        Path(ext_dir).mkdir(exist_ok=True)
        # Move the file to the respective directory
        shutil.move(os.path.join(directory, file), os.path.join(ext_dir, file))
    
    print(f"Files have been organized in {directory}")

if __name__ == "__main__":
    # Set the directory you want to organize
    dir_to_organize = input("Enter the directory to organize: ")
    if os.path.isdir(dir_to_organize):
        organize_files(dir_to_organize)
    else:
        print("The provided path is not a valid directory.")
