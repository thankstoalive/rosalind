import argparse

# Set parser
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int)
parser.add_argument('-k', type=int)
args = parser.parse_args()

# Get data
args = parser.parse_args()
n = args.n
k = args.k

# Get Answer

def f(n, k):
    if n==1:
        return 1
    elif n==2:
        return 1
    return f(n-1, k) + f(n-2, k) * k

print(f(n,k))


# f(1) = 1
# f(2) = 1
# f(3) = f(2) + f(1) * 3 = 4
# f(4) = f(3) + f(2) * 3 = 7
# f(5) = f(4) + f(3) * 3 = 19
# ...
# f(n) = f(n-1) + f(n-2) * k 


