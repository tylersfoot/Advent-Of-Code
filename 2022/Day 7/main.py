import os

def add_path(path, directories):
    if path not in directories.keys():
        directories[path] = 0
    return directories

def day6p1():
    f = open('input.txt')
    directories_size = {}
    current_stack = []
    current_path = ""
    for line in f:
        if line.startswith("$ cd"):
            print(line)
        if line[0].isdigit():
            file_size = int(line.split()[0])
            for directory in current_stack:
                directories_size[directory] += file_size
            print(line)
        print(line.rstrip("\n"))
    dirs = {} # directory and size
    return False

# def day6p2():
    
          
if __name__ == "__main__":
    print(os.listdir())
    print(day6p1())
