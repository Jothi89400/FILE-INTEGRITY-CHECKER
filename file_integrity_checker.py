import hashlib
import os
import json

# Function to calculate the hash of a file
def calculate_hash(file_path, hash_algorithm='sha256'):
    hash_func = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    return hash_func.hexdigest()

# Function to create a baseline of file hashes
def create_baseline(directory, output_file, hash_algorithm='sha256'):
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            baseline[file_path] = calculate_hash(file_path, hash_algorithm)

    with open(output_file, 'w') as f:
        json.dump(baseline, f, indent=4)

    print(f"Baseline created and saved to '{output_file}'.")

# Function to check for file changes against the baseline
def check_integrity(baseline_file, hash_algorithm='sha256'):
    try:
        with open(baseline_file, 'r') as f:
            baseline = json.load(f)
    except FileNotFoundError:
        print(f"Error: Baseline file '{baseline_file}' not found.")
        return

    current_state = {}
    for file_path in baseline.keys():
        current_state[file_path] = calculate_hash(file_path, hash_algorithm)

    for file_path, baseline_hash in baseline.items():
        current_hash = current_state.get(file_path)

        if current_hash is None:
            print(f"File missing: {file_path}")
        elif current_hash != baseline_hash:
            print(f"File changed: {file_path}")

    for file_path in current_state.keys() - baseline.keys():
        print(f"New file detected: {file_path}")

if __name__ == "__main__":
    print("File Integrity Checker")
    print("1. Create baseline")
    print("2. Check file integrity")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        directory = input("Enter the directory to monitor: ")
        output_file = input("Enter the output file for the baseline (e.g., baseline.json): ")
        create_baseline(directory, output_file)
    elif choice == '2':
        baseline_file = input("Enter the baseline file (e.g., baseline.json): ")
        check_integrity(baseline_file)
    else:
        print("Invalid choice. Please enter 1 or 2.")
