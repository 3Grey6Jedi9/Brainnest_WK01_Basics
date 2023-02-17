def func(filename):
    with open(filename, "r") as file:
        return file.read()


try:
    print(func("apple"))
except FileNotFoundError:
    print('The file was not found, please verify that you entered the right path')










