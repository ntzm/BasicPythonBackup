"""
Basic Python Backup
Nat Zimmermann
"""

# SETTINGS
TIME_FORMAT = '%d-%m-%Y-%H:%M:%S'
MAX_DIRS = 5

import shutil
from datetime import datetime
from os import walk


def remove_old_dirs():
    """Removes the oldest directories"""

    # Gets all immidiate directories
    dirs = walk('.').__next__()[1]
    dirs_date = []

    if len(dirs) > MAX_DIRS:
        test_dir = None

        for test_dir in dirs:
            try:
                app_dir = datetime.strptime(test_dir, TIME_FORMAT)
                dirs_date.append(app_dir)

            except ValueError:
                print("Directory %s does not match date format, ignoring..."
                      % test_dir)

        try:
            rm_dir = datetime.strftime(min(dirs_date), TIME_FORMAT)
            shutil.rmtree(rm_dir)

            print("Removed old directory %s" % rm_dir)

            remove_old_dirs()

        except IOError as error:
            print(error)


def copy_directory():
    """Copies a given directory to a new directory with the current date"""

    old_directory = input("Directory to copy: ")
    new_directory = datetime.now().strftime(TIME_FORMAT)

    print("Copying...")

    try:
        shutil.copytree(old_directory, new_directory)
        print("Successfully copied files to directory %s" % new_directory)

    except IOError as error:
        print(error)
        copy_directory()

copy_directory()
remove_old_dirs()
