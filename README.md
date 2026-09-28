# File Organizer

A simple Python automation tool that organizes files into separate folders based on their file extensions.

## Features

* Organizes files automatically by extension
* Creates folders automatically
* Supports different file types without hard-coding extensions
* Prevents files from being overwritten
* Renames duplicate files automatically
* Skips files without extensions
* Counts successfully organized files
* Handles file organization errors

## How It Works

The program asks the user for a folder path and scans the files inside it.

For each file, it:

1. Detects the file extension.
2. Creates a folder named after the extension.
3. Moves the file into the corresponding folder.
4. If a file with the same name already exists, it creates a new name such as `file_1.pdf`.

### Example

Before:

```text
TestFolder/
├── photo.jpg
├── document.pdf
├── data.xlsx
└── video.mp4
```

After running the program:

```text
TestFolder/
├── JPG/
│   └── photo.jpg
├── PDF/
│   └── document.pdf
├── XLSX/
│   └── data.xlsx
└── MP4/
    └── video.mp4
```

## Technologies Used

* Python
* OS module

## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run:

```bash
python file_organizer.py
```

5. Enter the path of the folder you want to organize.

## Example Output

```text
Starting file organization...

Organized: billing_data.xlsx → XLSX
Organized: Birth Certificate.jpeg → JPEG
Organized: ECAT - 2 Result 2026.pdf → PDF
Organized: ID Card Back Picture.jpg → JPG
Organized: WhatsApp Video 2026-09-27 at 7.09.24 PM.mp4 → MP4

================================
     ORGANIZATION COMPLETE
================================
Files organized: 5
================================
```

## Project Purpose

This project was built to practice Python automation, file handling, and working with the operating system using Python's `os` module.

## Author

Eman Fatima

GitHub: [emans-codes](https://github.com/emans-codes)
