# Import necessary modules
from pathlib import Path
import yaml
import logging
import argparse

#YAML import setup
def load_categories(yaml_path):
    try:
        # Attempt to open and load categories from 'categories.yaml'
        with open(yaml_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        # Log an error if 'categories.yaml' is not found
        logging.error(f"Categories file '{yaml_path}' not found. Please check the file path.")
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

#Create a command line
def parse_arguments():
    # Create an argument parser with a description of the script's purpose
    parser = argparse.ArgumentParser(description="Organize files based on categories.")
    
    # Define command-line arguments for specifying the initial directory and categories file
    parser.add_argument('--initial-dir', type=str, default='/home/audrey/Downloads', help="Which directory path would you like to organize?")
    parser.add_argument('--categories-file', type=str, default='categories.yaml', help="What file will you use as a reference to organize the categories?")
    
    # Parse the command-line arguments and return the resulting namespace
    return parser.parse_args()

def main():

    # Parse command-line arguments
    args = parse_arguments()

    # Configure logging for the entire application
    configure_logging()
    
    # Load categories from the specified file
    categories = load_categories(args.categories_file)

    if categories: 
         # Log an informational message about loading categories
        logging.info(f"Loaded categories from '{args.categories_file}'")

        # Organize files in the initial directory based on categories
        file_organizer(categories, Path(args.initial_dir))

        # Log an informational message about organizing the directory 
        logging.info(f"Directory '{args.initial_dir}' succesfully organized")
            
if __name__ == "__main__":
    # Execute the main function when the script is run
    main()



 










