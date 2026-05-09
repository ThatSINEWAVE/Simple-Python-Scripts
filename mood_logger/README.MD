# Mood Logger 

A Simple tool to track and log your daily mood.

## Features

- Log mod score (1 to 5) with date
- View recent history
- View statistical report including:
 - Average mood score
 - best and worst days
 - Score distribution 
 - longest logging streak

# Usage
For quick testing, you can run the code directly:
```python
# At the end of mood.py 
if __name__ == "__main__":
    mood_data = log_mood()
    save_mood(mood_data)
    show_history()
    show_report()
```

# Project Structure
```text
mood_logger/
    mood.py             # Main program file
    data/               # Data storage folder
        moods.json      # JSON file containing all mood data
    README.md           # This file
``` 
 

