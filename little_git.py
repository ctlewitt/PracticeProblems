# write a program that, given a directory name, makes a backup directory called name.bak
# with copies of everythign under the original directory

import shutil
import os


def little_git(src):
    shutil.copytree(src, src+".bak")

little_git("foo")