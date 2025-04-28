import os
from utils.organizer import organize_files
import logging

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs', 'organizer.log')

file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(log_formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])

def get_user_input():
    folder_path = input("Enter the folder path to organize: ")
    
    if not os.path.isdir(folder_path):
        # logging.error(f"Invalid directory: {folder_path}")
        print(f"Error: {folder_path} is not a valid directory.")
        return None, None
    
    print("\nHow would you like to organize your files?")
    print("1. By file type")
    print("2. By date")
    print("3. By both")
    
    method = input("Choose an option (1/2/3): ").strip()
    
    if method not in ["1", "2", "3"]:
        # logging.error("Invalid organization method selected")
        print("Invalid option. Please try again.")
        return None, None

    return folder_path, method

def main():
    folder_path, method = get_user_input()
    
    if folder_path is None:
        return

    organize_files(folder_path, method)
    print("Files have been organized successfully!")

if __name__ == "__main__":
    main()