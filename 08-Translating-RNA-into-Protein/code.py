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

# RNA codon table

map_dict = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
	    'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
	    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
	    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
	    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
	    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
	    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
	    'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
	    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
	    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
	    'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
	    'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
	    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
	    'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
	    'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
	    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}

answer_list = []

for idx in range(0, len(data), 3):
    sub_string = data[idx:idx+3]
    if sub_string in map_dict.keys():
        chr = map_dict[sub_string]
        if chr!='Stop':
            answer_list.append(chr)

answer = ''.join(answer_list)
print(answer)
