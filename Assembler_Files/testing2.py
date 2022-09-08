dict1 = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14}


a = [1 , dict1]

print(a[1]['K'])

def genA():
    for i in range(5):
        yield i
a
print(next(genA()))
