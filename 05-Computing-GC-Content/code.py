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

# Answer
max_value = 0
max_sid = ''

for string in data.split('>'):
    # pass if length is zero
    if len(string)==0:
        continue
    
    # split sample id and sequence
    temp = string.split('\n')
    sid = temp[0]
    seq = ''.join(temp[1:])
    
    # calculate GC_content
    n = len(seq)
    n_GC = sum([chr in ['G', 'C'] for chr in seq])
    GC_content = n_GC / n * 100

    # update max value
    if GC_content > max_value:
        max_value = GC_content
        max_sid = sid

print(max_sid)
print(max_value)
