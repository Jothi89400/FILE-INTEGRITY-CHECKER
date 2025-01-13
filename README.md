# FILE-INTEGRITY-CHECKER

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: JOTHILINGAM S

**INTERN ID**: CT08EAB

**DOMAIN**: Cyber Security & Ethical Hacking

**BATCH DURATION**: 5th, 2025 to February 5th, 2025

**MENTOR NAME**: NEELA SANTHOSH

###DESCRIPTION OF TASK PERFORMED

### Task Description: File Integrity Checker Development

The goal of this task was to develop a **File Integrity Checker** to monitor file changes in a directory using cryptographic hash values.
The tool calculates hash values for each file and compares them to detect changes, missing files, or new files. The task involves three 
key components: calculating file hashes, creating a baseline of file hashes, and checking file integrity.

**1. File Hash Calculation**

The `calculate_hash` function computes the hash of a file using a specified hashing algorithm (default: `sha256`). It reads the file in
binary mode and processes it in chunks to handle large files efficiently. The `hashlib.new()` method is used to initialize the hash 
function, ensuring compatibility with different algorithms.

**2. Creating the Baseline**

The `create_baseline` function creates an initial snapshot of a directory by calculating the hash values of all files in the directory and 
its subdirectories. The hashes are stored in a dictionary, which is then serialized into a JSON file. This file serves as a reference for 
later integrity checks.

**3. Checking File Integrity**

The `check_integrity` function compares the current state of files against the baseline. It recalculates the hashes for each file and compares
them with the baseline. If a file’s hash differs, it indicates the file has changed. Missing files or new files are also reported.

**4. Command-Line Interface (CLI)**

The script offers a simple CLI that allows users to choose between creating a baseline or checking integrity. When creating a baseline, the
user provides the directory and the output file for the baseline. When checking integrity, the user provides the baseline file for comparison.

**5. Error Handling and Optimization**

The script handles errors like missing files or permission issues without crashing. It also optimizes memory usage by processing files in 
chunks, making it efficient for larger directories and files.

# OUTPUT

![file integrity checker output](https://github.com/user-attachments/assets/763fecf1-7fed-46fe-ac5b-2800dcf960d4)


