import argparse

# Set parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', type=str)
args = parser.parse_args()

# Get data
args = parser.parse_args()
input_string = args.input

# Transcribing DNA into RNA
print(input_string.replace('T', 'U'))

