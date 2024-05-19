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

# Get Answer
S = data.split('\n')[0]
t = data.split('\n')[1]

for idx in range(len(S)-len(t)+1):
    S_subset = S[idx:idx+len(t)]
    if S_subset==t:
        print(idx+1, end=' ')

