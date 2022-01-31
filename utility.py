import os
import sys
import shutil
import subprocess
import threading


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

# Run a shell command and yield lines of text as it prints anything out
def run(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode("utf-8").strip().replace("> ", "")
        if output == "" and process.poll() is not None:
            break
        if output:
            yield output
    rc = process.poll()
    return rc

def sr_command(sr_path, command, console=True, display_error=True):
    print("\n" + command + "\n")
    for line in run(command):
        if console:
            print(line)
        elif display_error and line.startswith("ERROR"):
            print(line)
            console = True

def sr_dump(sr_path, console=True, display_error=True):
    command = f"{sr_path}StarRod.exe -DUMPASSETS"
    thread = threading.Thread(target=sr_command, args=[sr_path, command, console, display_error])
    thread.start()
    return thread

def sr_copy(sr_path, console=True, display_error=True):
    command = f"{sr_path}StarRod.exe -COPYASSETS"
    thread = threading.Thread(target=sr_command, args=[sr_path, command, console, display_error])
    thread.start()
    return thread

def sr_compile(sr_path, console=True, display_error=True):
    command = f"{sr_path}StarRod.exe -COMPILEMOD"
    thread = threading.Thread(target=sr_command, args=[sr_path, command, console, display_error])
    thread.start()
    return thread