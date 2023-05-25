import argparse

parser = argparse.ArgumentParser(prog='gendiff',
                                 description='Compares two configuration files and shows a difference.',
                                 epilog='Text at the bottom of help')

parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()
print(args)


