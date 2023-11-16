import os
import shutil
from pathlib import Path

# Define file categories and their corresponding file extensions
categories = {"Audios": [".aif", ".cda", ".mid.mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl", ".midi"],
            "Compressed": [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar", ".z", ".zip", ".gz"],
            "Documents": [".bin", ".dmg", ".iso", ".toast", ".vcd", ".csv", ".dat", ".db", ".log", ".mdb", ".sav",
                          ".sql", ".tar", ".xml", ".dbf", ".email", ".eml", ".emlx", ".msg", ".oft", ".ost", ".pst",
                          ".vcf", ".asp", ".cer", ".cfm", ".cgi", ".css", ".htm", ".js", ".jsp", ".part", ".php", ".py",
                          ".rss", ".xhtml", ".fnt", ".fon", ".otf", ".ttf", ".doc", ".odt", ".pdf", ".rtf", ".tex",
                          ".txt", ".wpd", ".key", ".odp", ".pps", ".ppt", ".pptx", ".c", ".cgi", ".class", ".cpp",
                          ".cs", ".h", ".java", ".php", ".py", ".sh", ".swift", ".vb", ".ods", ".xls", ".xlsm", ".xlsx",
                          ".docx", ".aspx", ".html"],
            "Images": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".png", ".ps", ".psd", ".svg", ".tif", ".jpg", ".tiff"],
            "Videos": [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg.rm", ".swf",
                       ".vob", ".wmv", ".mpeg", ".webm"],
            "Setups": [".apk", ".bat", ".bin", ".cgi", ".com", ".exe", ".gadget", ".jar", ".msi", ".py", ".wsf"],
            "Systemfiles": [".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ico", ".ini",
                            ".lnk", ".msi",
                            ".sys", ".tmp"]}

# Assign the initial directory
initial_dir = '/path/to/dir/to/organize'
 
# Iterate over files in the initial directory
files = Path(initial_dir).glob('*')
for file in files:
    # Get the file extension
    extension = file.suffix.lower()

    # Check the file extension against categories dictionary
    for key, value in categories.items():
        if extension in value:
            cat_dir = initial_dir + "/" + key
            # Create a directory for the category if it doesn't exist
            if not os.path.exists(cat_dir):
                os.makedirs(cat_dir)
            # Move the file to the corresponding category directory
            destination = f'{cat_dir}/{file.name}'
            shutil.move(str(file), destination)
            break


            
            




 