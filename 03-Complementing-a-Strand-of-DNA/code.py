import argparse

# Set parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', type=str)
args = parser.parse_args()

# Get data
args = parser.parse_args()
input_string = args.input

# Complementing a Strand of DNA

map_dict = {'A':'T',
	    'T':'A',
	    'C':'G',
	    'G':'C'}

new_string = ''.join([map_dict[i] for i in input_string[::-1]])

print(new_string)


