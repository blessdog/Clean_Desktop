import os
import shutil
from datetime import datetime

# set up folder paths
desktop_path = os.path.expanduser("~/Desktop")
folder_names = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Documents": ["doc", "docx", "pdf", "txt"],
    "Videos": ["mp4", "avi", "mov", "mkv"],
}

# create folders if they don't exist
for folder_name in folder_names.keys():
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# get today's date in YYYY-MM-DD format
today = datetime.today().strftime('%Y-%m-%d')

# loop over files on desktop
for file_name in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file_name)
    # check if file is not a folder and has an extension
    if os.path.isfile(file_path) and "." in file_name:
        # get file extension
        file_extension = file_name.split(".")[-1].lower()
        # loop over folder names and move file to appropriate folder
        for folder_name, extensions in folder_names.items():
            if file_extension in extensions:
                folder_path = os.path.join(desktop_path, folder_name)
                new_file_name = f"{today}_{file_name}"
                new_file_path = os.path.join(folder_path, new_file_name)
                shutil.move(file_path, new_file_path)
                break

