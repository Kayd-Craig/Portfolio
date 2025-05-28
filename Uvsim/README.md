# UVSim README

## Overview

UVSim is a software simulator designed to help computer science students understand machine language and computer architecture. It interprets and executes a machine language called BasicML by loading programs into memory and simulating basic operations such as reading input, writing output, performing arithmetic, and managing control flow.

## Prerequisites

Before running UVSim, ensure the following:

- **Python 3.x**: Required to run the UVSim code.
- **No additional libraries**: The simulator relies only on Python’s standard library.
- **Program files**: UVSim requires input files in `.txt` format, containing BasicML code.

## Running the Application

### Launching

To start UVSim:

1. **Execute main.py**: Double-click `main.py` or open it with Python. If double-clicking doesn’t work, right-click the file and select ‘Open with’ → ‘Python’ or ‘Python 3.x’ (not IDLE).
   
2. **Command line option**: Navigate to the program directory and enter one of these commands:
   ```bash
   python main.py
   ```
   or
   ```bash
   py main.py
   ```

Upon launching, a GUI window will open. To start a simulation, follow these steps:

1. Click the **'Open File'** button to open files into **File Memory**.
2. File Memory will display all open files, allowing users to manage multiple files at once. Select a file from File Memory to load its contents into the editor, where it can be viewed or modified.
3. Once a file is in the editor, click **'Run'** to load the program into UVSim memory and execute it.
4. To run another file, simply select a different file from File Memory, and click **'Run'** again.

### Note on Address Space and File Limits

UVSim can address up to **1000 lines** of memory, but each program file loaded or edited should contain **no more than 250 lines**. Commands referencing line numbers outside the **000–249** range will be considered invalid and may halt execution.

### Word Size and Overflow Handling

UVSim supports **six-digit word size**, which allows for extended arithmetic. Overflow handling is managed for six-digit operations, which may alter the result for operations that previously overflowed in a four-digit context. Ensure values do not exceed six digits to maintain accuracy.

### Function Code Update

All function codes are now six digits, with a leading zero added to the original format (e.g., `010` instead of `10` for READ commands). This aligns with UVSim’s six-digit word size and maintains backward compatibility.

### File Compatibility

UVSim supports **both four-digit and six-digit word files**. The simulator detects the word size at load time to handle each format accordingly. However, **do not mix four- and six-digit words within a single file**; each file must adhere consistently to one format.

## User Input

When running BasicML programs with READ instructions (opcode `10`), UVSim prompts the user:  
**"Enter the word going into register __:"**

Enter the integer (up to six digits, positive or negative) in the text field at the bottom of the GUI and either press **'Enter'** on your keyboard or click the **'Enter'** button to submit.

## Output

For WRITE instructions (opcode `11`), UVSim outputs the contents of the specified memory location to the output area, which appears as a large box in the middle of the GUI.

## Saving Files

UVSim provides **Save** and **Save As** options for file management:

- **Save**: Modifies the existing file if previously opened. If no file is loaded, this option functions like **Save As**, prompting you to create a new file.
- **Save As**: Opens a file explorer to name and save data as a new file in a chosen location.

## Changing the Theme

UVSim allows customization of the GUI theme through a `config.ini` file:

1. Ensure the `config.ini` file contains valid hexadecimal color codes for primary and secondary colors as follows:
   ```ini
   [Theme]
   primary_color = #4C721D
   secondary_color = #FFFFFF
   ```
   - **Primary Color**: Backgrounds and main frames.
   - **Secondary Color**: Button text and GUI text color.

2. Place `config.ini` in the same directory as `UVSim.exe`. If the file is missing or malformed, a default will be generated upon execution.

## Error Handling

Errors encountered during execution will display in the output area:

- **Fatal errors**: Halt the simulator.
- **Warnings**: Display a message but allow the simulation to proceed as possible.

## Files

UVSim’s codebase comprises the following files:

- **main.py**: Entry point for running UVSim.
- **uvsim.py**: Contains the UVSim class and logic for simulating BasicML operations.
- **gui.py**: Manages the TKinter GUI.
- **config.py**: Handles the GUI theming and color logic.
- **events.py**: Event manager for coordinating GUI and main program logic.
- **tests/**: Directory containing unit tests and sample BasicML programs.
  - Note: Tests may need adjustment if stored in a different directory from the main codebase.
- **README.md**: This file, providing instructions for launching and using UVSim.
