import sys
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

# get sequence
seq_list = []
for lines in data.split('>'):
    seq = ''.join(lines.split('\n')[1:])
    if len(seq)>0:
        seq_list.append(seq)

# get max_sequence and count
max_seq = ''
count_dict = {}
count_dict['A'] = []
count_dict['C'] = []
count_dict['G'] = []
count_dict['T'] = []

len_seq = len(seq_list[0])

for chr in ['A', 'C', 'G', 'T']:
    for idx in range(len_seq):
        n=len([seq for seq in seq_list if seq[idx]==chr])
        count_dict[chr].append(n)

for idx in range(len_seq):
    n_a = count_dict['A'][idx]
    n_c = count_dict['C'][idx]
    n_g = count_dict['G'][idx]
    n_t = count_dict['T'][idx]
    temp = [n_a, n_c, n_g, n_t]
    max_index = temp.index(max(temp))
    max_chr = ['A', 'C', 'G', 'T'][max_index]
    max_seq = max_seq + max_chr

sys.stdout = open('/Users/younghyun/github/rosalind/10-Consensus-and-Profile/output.txt', 'w')
print(max_seq)
print(f"A: {' '.join(map(str, count_dict['A']))}")
print(f"C: {' '.join(map(str, count_dict['C']))}")
print(f"G: {' '.join(map(str, count_dict['G']))}")
print(f"T: {' '.join(map(str, count_dict['T']))}")
sys.stdout.close()
