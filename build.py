import os
import shutil

os.system("pyinstaller main.spec")
shutil.copy("./dist/main.exe", "./")
shutil.rmtree("./dist")