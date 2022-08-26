import os


def rename():
    directory = r"C:\Users\Krystian\Desktop\dataset\labels\val"
    dir = os.listdir(directory)
    char = '.'
    ch = '.txt'

    for file in dir:
        old_name = os.path.join(directory, file)
        # new_name = file.split(char, 1)[0]
        new_name = old_name + ch
        os.rename(old_name, new_name)


rename()
