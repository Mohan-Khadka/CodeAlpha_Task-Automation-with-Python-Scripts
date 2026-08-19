**Task Automation with Python Scripts**
# Automatic Task Automation 

A Python-based automation project designed to automate common repetitive tasks such as organizing image files, extracting email addresses from text files, and scraping webpage titles.

---

## Project Overview

**Automatic Task Automation** is a Python project that combines multiple small automation utilities into a single menu-driven application.

The project automates three practical tasks:

1. **Image File Organizer** — Finds supported image files and moves them into an organized folder.
2. **Email Address Extractor** — Extracts email addresses from a `.txt` file and saves them into another file.
3. **Webpage Title Scraper** — Retrieves the title of a fixed webpage and saves it into a text file.

The project also provides a **main menu system** that allows the user to run individual tasks or all tasks together.

---

## Objectives

The main objectives of this project are:

* Automate repetitive file-management tasks.
* Practice Python file and folder handling.
* Work with regular expressions.
* Learn basic web scraping.
* Use Python modules effectively.
* Implement functions and modular programming.
* Handle errors safely.
* Create a simple command-line menu system.
* Generate and manage output files automatically.

---

## Features

### 1. Image File Organizer

The Image File Organizer automatically detects image files and moves them from the source folder to `Organized_Images`.

Supported image formats include:

* `.jpg`
* `.jpeg`
* `.png`
* `.gif`
* `.bmp`
* `.webp`
* `.tiff`
* `.tif`
* `.svg`
* `.ico`

The program also:

* Detects uppercase extensions such as `.JPG` and `.PNG`.
* Automatically creates the destination folder.
* Skips non-image files.
* Handles duplicate filenames safely.
* Displays moved and skipped files.
* Displays a final summary.

### Image Workflow
```text
Initial_images/
       |
       v
Scan files
       |
       v
Check image extension
       |
       +---- Not an image ----> Skip
       |
       v
Move image
       |
       v
Organized_Images/
```

---

## 2. Email Address Extractor

The Email Address Extractor reads text from:
```text
email_data/contacts.txt
```

It uses Python's `re` module to identify email addresses.

The extracted email addresses are saved to:
```text
output/extracted_emails.txt
```

### Features

* Reads `.txt` files.
* Uses Regular Expressions (`re`).
* Extracts email addresses automatically.
* Removes duplicate email addresses.
* Preserves the order of discovered emails.
* Creates the output folder automatically.
* Handles missing input files.
* Handles empty input files.
* Displays the number of extracted emails.

### Email Workflow
```text
contacts.txt
      |
      v
Read text
      |
      v
Regular Expression
      |
      v
Find email addresses
      |
      v
Remove duplicates
      |
      v
extracted_emails.txt
```

### Example

Input:
```text
Hello, my name is Ram.
My email is ram@gmail.com.

You can contact Sita at sita@gmail.com.
Another email is ram@gmail.com.

Company contact: info@company.org
```

Output:
```text
ram@gmail.com
sita@gmail.com
info@company.org
```

---

## 3. Webpage Title Scraper

The Webpage Title Scraper connects to a fixed webpage using the `requests` library.

Current webpage:
```text
https://example.com
```

The program:

1. Sends an HTTP GET request.
2. Receives the webpage HTML.
3. Finds the `<title>` tag.
4. Extracts the webpage title.
5. Saves the title to:
```text
output/webpage_title.txt
```

### Webpage Workflow

```text
Fixed Webpage
      |
      v
HTTP GET Request
      |
      v
HTML Response
      |
      v
Find <title>
      |
      v
Extract Title
      |
      v
webpage_title.txt
```

### Error Handling

The scraper handles:

* No internet connection
* Connection timeout
* HTTP request errors
* Missing title tag
* Unexpected errors

---

# Project Structure
```text
Automatic Task Automation/
│
├── main.py
├── image_file_organizer.py
├── email_extractor.py
├── webpage_title_scraper.py
├── README.md
│
├── images/
│   ├── photo1.jpg
│   ├── photo2.png
│   ├── photo3.jpeg
│   └── photo4.webp
│
├── Initial_images/
│   ├── image.png
│   ├── image1.webp
│   ├── image2.webp
│   ├── image3.webp
│   ├── image4.webp
│   └── image5.webp
│
├── Organized_Images/
│   ├── image.png
│   ├── image1.webp
│   └── image2.webp
│
├── email_data/
│   └── contacts.txt
│
└── output/
    ├── extracted_emails.txt
    └── webpage_title.txt
```

> `Organized_Images/` and the output files can be created automatically by the program when they do not already exist.

---

# Technologies Used

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| Python             | Main programming language      |
| `os`               | File and folder operations     |
| `shutil`           | Moving image files             |
| `re`               | Extracting email addresses     |
| `requests`         | Sending HTTP requests          |
| File Handling      | Reading and writing text files |
| Exception Handling | Handling runtime errors        |
| Functions          | Organizing program logic       |
| CLI Menu           | User interaction               |

---

# Python Concepts Used

This project demonstrates several important Python concepts.

## 1. Modules

The project uses Python modules such as:
```python
import os
import shutil
import re
import sys
import requests
```

---

## 2. Functions

Each automation task is implemented using a separate function.

Examples:
```python
organize_images()
```

```python
extract_emails()
```
```python
scrape_webpage_title()
```

This keeps the code organized and reusable.

---

## 3. File Handling

The project reads and writes text files using:
```python
with open(filename, "r", encoding="utf-8") as file:
```

and:
```python
with open(filename, "w", encoding="utf-8") as file:
```

---

## 4. Regular Expressions

The Email Extractor uses the `re` module to identify email addresses from text.

Example pattern:
```python
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```

---

## 5. File and Folder Operations

The Image Organizer uses:
```python
os.listdir()
os.path.exists()
os.path.isdir()
os.path.isfile()
os.path.splitext()
os.makedirs()
```

The project uses `shutil.move()` to move image files.

---

## 6. Web Requests

The Webpage Title Scraper uses:
```python
requests.get()
```

to retrieve webpage content.

---

## 7. Exception Handling

The project uses `try` and `except` to prevent unexpected errors from crashing the application.

For example:
```python
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.Timeout:
    print("Connection timeout.")
```

---

## 8. User Input and Menu System

The `main.py` file provides a command-line menu:
```text
==================================================
       AUTOMATIC TASK AUTOMATION
==================================================

1. Image File Organizer
2. Email Address Extractor
3. Webpage Title Scraper
4. Run All Tasks
5. Exit

Enter your choice:
```

The user can select which automation task to execute.

---

# Installation

## Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:
```bash
python --version
```

On some Linux systems:
```bash
python3 --version
```

---

## Step 2: Install Required External Library

Most modules used in this project are built into Python.

### Built-in modules
```text
os
shutil
re
sys
```

No separate installation is required for them.

### External module

The Webpage Title Scraper requires:
```text
requests
```

Install it using:
```bash
pip install requests
```

If required:
```bash
pip3 install requests
```

---

# How to Run

Open the terminal inside the project directory:
```bash
cd "Automatic Task Automation"
```

Run:
```bash
python main.py
```

Or on systems where `python3` is required:
```bash
python3 main.py
```

---

# Main Menu

After running `main.py`, the application displays:
```text
==================================================
       AUTOMATIC TASK AUTOMATION
==================================================
1. Image File Organizer
2. Email Address Extractor
3. Webpage Title Scraper
4. Run All Tasks
5. Exit
==================================================
```

---

# Menu Options

## Option 1 — Image File Organizer

Select:
```text
1
```

The program scans the configured image source folder, identifies supported image files, and moves them to:

```text
Organized_Images/
```

---

## Option 2 — Email Address Extractor

Select:
```text
2
```

The program reads:
```text
email_data/contacts.txt
```

and saves the extracted unique email addresses to:
```text
output/extracted_emails.txt
```

---

## Option 3 — Webpage Title Scraper

Select:
```text
3
```

The program accesses the fixed webpage:
```text
https://example.com
```

and saves its title to:
```text
output/webpage_title.txt
```

An active internet connection is required.

---

## Option 4 — Run All Tasks

Select:
```text
4
```

This runs:
```text
Image File Organizer
        ↓
Email Address Extractor
        ↓
Webpage Title Scraper
```

All three automation tasks are executed sequentially.

---

## Option 5 — Exit

Select:
```text
5
```

to safely exit the program.

---

# Example Output

A successful run may display:
```text
==================================================
       AUTOMATIC TASK AUTOMATION
==================================================
1. Image File Organizer
2. Email Address Extractor
3. Webpage Title Scraper
4. Run All Tasks
5. Exit
==================================================

Enter your choice (1-5): 4
```

The program then executes all three tasks and displays their individual results and summaries.

---

# Output Files

After successful execution, the project can produce:

### Image Output
```text
Organized_Images/
```

Contains the organized image files.

### Email Output
```text
output/extracted_emails.txt
```

Contains unique extracted email addresses.

### Webpage Output
```text
output/webpage_title.txt
```

Contains the scraped webpage title.

---

# Error Handling

The project includes handling for common problems.

### Missing Image Folder

If the expected image source folder does not exist, the program can create the required folder.

### Empty Folder

The program informs the user when there are no files to process.

### Duplicate Image Names

If an image with the same filename already exists in the destination folder, the program creates a new filename instead of overwriting the existing file.

Example:
```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

### Missing Contacts File

The Email Extractor can create the required `contacts.txt` file when it is missing.

### Empty Contacts File

If the text file is empty, the program displays an appropriate message.

### No Email Addresses

If no email address is found, the program informs the user.

### Internet Error

The Webpage Title Scraper handles:

* Connection errors
* Timeout errors
* HTTP request errors
* Missing webpage title
* Unexpected errors

### Invalid Menu Input

If the user enters an invalid menu option, the program asks for a valid choice instead of crashing.

---

# Testing

## Test 1: Image Organizer

1. Put different image files inside the source image folder.
2. Run:

```bash
python main.py
```

3. Select:
```text
1
```

4. Check:
```text
Organized_Images/
```

---

## Test 2: Email Extractor

1. Open:
```text
email_data/contacts.txt
```

2. Add text containing email addresses.
3. Run the program.
4. Select:

```text
2
```

5. Check:
```text
output/extracted_emails.txt
```

---

## Test 3: Webpage Scraper

1. Make sure you have an internet connection.
2. Run:
```bash
python main.py
```

3. Select:
```text
3
```

4. Check:
```text
output/webpage_title.txt
```

---

## Test 4: Run All Tasks

Run:
```bash
python main.py
```

Then select:
```text
4
```

Verify:
```text
Organized_Images/
output/extracted_emails.txt
output/webpage_title.txt
```

---

# Real-Life Use Cases

This project demonstrates how Python automation can be useful in real situations.

### Image Organization

Useful for organizing large collections of:

* Photos
* Screenshots
* Downloaded images
* Project assets

### Email Extraction

Useful when processing:

* Contact lists
* Text documents
* Customer information
* Business documents

### Webpage Title Scraping

Useful for:

* Collecting webpage information
* Basic web-data extraction
* Automating repetitive web checks
* Learning web scraping fundamentals

---

# Project Workflow
```text
                    AUTOMATIC TASK AUTOMATION
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
       Image Organizer   Email Extractor   Webpage Scraper
             |                |                |
             v                v                v
      Organize Images    Find Emails       Get Title
             |                |                |
             v                v                v
    Organized_Images/   extracted_emails   webpage_title
```

---

# Future Improvements

Possible future improvements include:

* Support for more image formats.
* Recursive scanning of subfolders.
* A graphical user interface (GUI).
* Progress bars.
* Configurable source and destination folders.
* User-provided webpage URLs.
* More advanced email validation.
* CSV export for extracted emails.
* Logging system.
* Scheduled automation.
* File sorting by date or file type.
* Improved HTML parsing using BeautifulSoup.

---

# Learning Outcomes

After completing this project, the following concepts can be practiced:

* Python modules
* Functions
* File handling
* Directory management
* File movement
* Regular expressions
* HTTP requests
* Basic web scraping
* Exception handling
* User input
* Menu-driven programs
* Modular programming
* Automation concepts

---

# Conclusion

**Automatic Task Automation** demonstrates how Python can be used to reduce repetitive manual work.

By combining file management, regular expressions, web requests, file handling, and a command-line menu system, the project provides a practical introduction to Python automation.

The project shows how a simple Python script can turn repetitive tasks into automated workflows that are faster, more consistent, and easier to manage.

---
## Internship Task

**Program:**      Python Programming Internship
**Organization:** CodeAlpha
**Task:**         Task 3 – Task Automation with Python Scripts
**Language:**     Python
**Project Type:** Console-Based Automation Project


## Author

**Mohan Khadka**

Python Automation Project

---

## License

This project is created for educational and internship purposes.
