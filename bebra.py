import os

os.system("ls | nl")

os.system("cd $(ls | sed -n 1p)")
