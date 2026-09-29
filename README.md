# Docufix

A command-line Python tool that reads a text file, fixes its capitalization, prints a statistics report, and saves the corrected text to a new file.

## Overview

The program asks for an input filename and an output filename, reads the input text, and normalizes its capitalization: everything is lowercased, then the first letter of each sentence (after `.`, `?` or `!`) is capitalized. It then prints a "Document Processing Report" and writes the corrected text to the output file. You can process multiple files in one session.

## Features

- Reads any plain-text (`.txt`) file
- Automatic sentence-case correction
- Report with:
  - Total word count
  - Unique vocabulary size (case-insensitive)
  - Total number of character corrections made
  - Top 5 most frequent words
  - The corrected text
- Saves corrected text to a user-specified output file
- Option to process another file without restarting

## Technologies / Tools Used

- Python 3.8+ (standard library only, no external dependencies)
- Git & GitHub for version control

## Installation & Running

1. Clone the repository:
   ```bash
   git clone https://github.com/<Aditya-singh-2007/docufix.git
   cd <docufix>
   ```
2. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
3. Run the program:
   ```bash
   python main.py
   ```
4. When prompted, enter the input filename (e.g. `text.txt`) and the output filename (e.g. `updated_text.txt`). Both paths are relative to where you run the script.
5. Answer `y` or `yes` when asked to process another file, or anything else to exit.

## Testing

Manual test steps:

1. Create `text.txt` containing:
   ```
   hello world. this IS a test! do you agree? yes it works.
   ```
2. Run `python main.py`, input `text.txt` and `updated_text.txt`.
3. Check the console report and open `updated_text.txt`. Expected output:
   ```
   Hello world. This is a test! Do you agree? Yes it works.
   ```
4. Edge cases to try:
   - An empty file
   - A file with no punctuation
   - A file with multiple blank lines or numbers
   - A non-existent input filename (currently raises `FileNotFoundError`)

## Sample Output

```
==========================================
       DOCUMENT PROCESSING REPORT
==========================================
Total Words:  11
Unique Vocabulary Size: 10
Total Corrections:  9
Top 5 Words:  [...]
Corrected Text: Hello world. This is a test! ...
==========================================
```

## Screenshots

_Add screenshots of the terminal output here, e.g. `![Report](screenshots/report.png)`_

## Project Structure

```
.
├── main.py          # Source code
├── README.md        # Project documentation
├── statement.md     # Problem statement and scope
└── text.txt         # Sample input file
```
