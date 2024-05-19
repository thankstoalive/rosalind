import argparse

# Set parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', type=str)
args = parser.parse_args()

# Get data
args = parser.parse_args()
input_string = args.input

# Create variavles
count_A = 0
count_C = 0
count_T = 0
count_G = 0

# Counting DNA Nuvleotids
for char in input_string:
  if char=='A':
    count_A += 1
  elif char=='C':
    count_C += 1
  elif char=='T':
    count_T += 1
  elif char=='G':
    count_G += 1

print(count_A, count_C, count_G, count_T)
