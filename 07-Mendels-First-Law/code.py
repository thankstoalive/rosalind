import argparse

# Set parser
parser = argparse.ArgumentParser()
parser.add_argument('-k', type=int)
parser.add_argument('-m', type=int)
parser.add_argument('-n', type=int)
args = parser.parse_args()

# Get data
args = parser.parse_args()
k = args.k
m = args.m
n = args.n

# calculate answer
N = (k+m+n)*(k+m+n-1)*4/2
n_c1 = max([k*(k-1)/2*4, 0])
n_c2 = k*m*4
n_c3 = k*n*4
n_c4 = max([m*(m-1)/2*3, 0])
n_c5 = m*n*2

answer = (n_c1 + n_c2 + n_c3 + n_c4 + n_c5) / N
print(answer)


# case1) (AA, AA) -> AA:4
# case2) (AA, Aa) -> AA:2, Aa:2
# case3) (AA, aa) -> Aa:4
# case4) (Aa, Aa) -> AA:1, Aa:2, aa:1
# case5) (Aa, aa) -> Aa:2, aa:2
# case6) (aa, aa) -> aa:4

