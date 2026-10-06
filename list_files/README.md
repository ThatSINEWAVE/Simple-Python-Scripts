# List Files Script

This is a simple Python script that lists all files and directories in a specified folder.

## Features

* Lists files and folders in any directory
* Handles errors (missing folder or no access)
* Interactive input (asks user for a path)
* Beginner-friendly and easy to understand

## Usage

Run the script:

```bash
python list_files.py
```

You will be prompted to enter a folder path:

```
Enter folder path (leave empty for current directory):
```

* Press **Enter** to use the current directory
* Or type a path, for example:

```
/home/user
```

## Example Output

```
file1.py
file2.txt
folder1
```

## Using in Code

You can also import and use the function in your own Python code:

```python
from list_files import list_files

list_files("your/folder/path")
```

## Requirements

* Python 3.x

## Notes

* If the directory does not exist, an error message will be shown
* If access is denied, the script will notify you
