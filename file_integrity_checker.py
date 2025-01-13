import hashlib
import os
import time

# Function to calculate hash of a file
def calculate_hash(file_path, hash_algorithm='sha256'):
    hash_obj = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read the file in chunks
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# Function to monitor file integrity
def monitor_file_integrity(file_path, hash_algorithm='sha256', interval=10):
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return
    
    print(f"Monitoring file: {file_path}")
    initial_hash = calculate_hash(file_path, hash_algorithm)
    print(f"Initial {hash_algorithm.upper()} hash: {initial_hash}")

    while True:
        time.sleep(interval)  # Wait for the specified interval before checking again
        current_hash = calculate_hash(file_path, hash_algorithm)    
        if current_hash != initial_hash:
            print(f"WARNING: File integrity compromised! Hash changed.")
            print(f"Old Hash: {initial_hash}")
            print(f"New Hash: {current_hash}")
            initial_hash = current_hash  # Update hash to the new value
        else:
            print(f"File {file_path} is intact.")

# Example usage
file_to_monitor = 'C:\\Users\\LENOVO\\Documents\\text file.txt'  # Replace with the file you want to monitor
monitor_file_integrity(file_to_monitor)


