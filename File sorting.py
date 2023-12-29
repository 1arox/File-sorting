import os
import shutil

# Path to your Downloads folder (change this to your actual Downloads path)
# Make sure to use the correct path for your system
downloads_path = r'C:\Users\aribe\Downloads'

# File type categorization
file_categories = {
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.gz', '.tar'],
    'Others': []  # Files that don't fit in above categories
}

# Create categorized folders if they don't exist
for category in file_categories:
    #Constructs the full path for the category folder.
    folder_path = os.path.join(downloads_path, category)
    # Checks if the folder for this category doesn't exist.
    if not os.path.exists(folder_path):
        # Creates the folder for the current category
        os.mkdir(folder_path)


# Organize files
 # Loops through each file in the Downloads directory    
for filename in os.listdir(downloads_path):
    #Checks if the current item is a file.
    if os.path.isfile(os.path.join(downloads_path, filename)):
        #Extracts the file extension and converts it to lowercase.
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        # Loops over each category and its associated extensions
        for category, extensions in file_categories.items():
            #Checks if the file's extension matches the current category
            if file_ext in extensions:
                try:
                    # Moves the file to the appropriate category folder
                    shutil.move(os.path.join(downloads_path, filename),
                                os.path.join(downloads_path, category, filename))
                    moved = True
                    #Catches permission errors that might occur during the move
                except PermissionError:
                    print(f"Couldn't move {filename}: File is in use or access is denied.")
                    break

        if not moved:
            # Try to move to 'Others' if the file type is not recognized
            try:
                #Attempts to move the file to the 'Others' folder.
                shutil.move(os.path.join(downloads_path, filename),
                            os.path.join(downloads_path, 'Others', filename))
            # Catches permission errors for this operation    
            except PermissionError:
                print(f"Couldn't move {filename}: File is in use or access is denied.")
#Prints a confirmation
print("Files organized.")

