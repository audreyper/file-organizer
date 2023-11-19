# Import necessary modules
from pathlib import Path
import yaml
import logging

# YAML import setup
def load_categories(yaml_path):
    try:
        # Attempt to open and load categories from 'categories.yaml'
        with open('categories.yaml', 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        # Log an error if 'categories.yaml' is not found
        logging.error(f"Categories file '{yaml_path}' not found.")
    except yaml.YAMLError as e:
        # Log an error if there's an issue loading categories from the file
        logging.error(f"Error loading categories: {e}")
     
# Iterate over files in the initial directory
def file_organizer(categories, initial_dir_path):
    # Get a list of files in the specified directory
    files = initial_dir_path.glob('*')
    for file in files:
        # Get the file extension
        extension = file.suffix.lower()
        # Call the mover function to organize the file
        mover(extension, file, categories, initial_dir_path)


def mover(extension, file, categories, initial_dir_path): 
    # Check the file extension against categories dictionary
    for key, value in categories.items():
        if extension in value:
            # Create a directory for the category if it doesn't exist
            cat_dir = initial_dir_path / key
            cat_dir.mkdir(parents=True, exist_ok=True)
            # Move the file to the corresponding category directory
            destination = cat_dir / file.name
            file.rename(destination)
            break

def configure_logging():
    # Configure logging with a StreamHandler to display log messages on the console
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()])


def main():
    # Configure logging for the entire application
    configure_logging()

    # Define the initial directory path and the categories file path
    initial_dir_path = Path('/home/audrey/Downloads')
    categories_file_path = 'categories.yaml'
    
    # Load categories from the specified file
    categories = load_categories(categories_file_path)

    if categories: 
        # Organize files in the initial directory based on categories
        file_organizer(categories, initial_dir_path)
            
if __name__ == "__main__":
    # Execute the main function when the script is run
    main()



 










