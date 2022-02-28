import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Get a list of files in a directory with specific filetypes
def get_files(directory_name, **kwargs):
    if filetype := kwargs.get("filetype"):
        filetypes = [filetype]
    else:
        filetypes = kwargs.get("filetypes", None)

    files = list()
    for entry in os.listdir(directory_name):
        full_path = os.path.join(directory_name, entry)
        if os.path.isdir(full_path):
            files += get_files(full_path, filetypes=filetypes)
        else:
            if not filetypes:
                files.append(full_path)
            elif any([full_path.endswith(ftype) for ftype in filetypes]):
                files.append(full_path)

    return files