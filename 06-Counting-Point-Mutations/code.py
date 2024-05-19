import argparse

# Set parser
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', dest='path', type=str)
args = parser.parse_args()

# Get data
args = parser.parse_args()
path = args.path

f = open(path, 'r')
data = f.read()

# Counting Point Mutations
n = 0

str1 = data.split('\n')[0]
str2 = data.split('\n')[1]

for chr1, chr2 in zip(str1, str2):
    if chr1!=chr2:
        n+=1

print(n)


