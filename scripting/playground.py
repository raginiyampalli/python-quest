import os
import time


def print_current_working_directory():
    print("Here is the current working directory :")
    print(os.getcwd())
    print(time.localtime(time.time()))


"""Testing above functions"""
print_current_working_directory()