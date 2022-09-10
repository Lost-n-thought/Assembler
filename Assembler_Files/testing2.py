import fileinput
import SymbolTableGenration as SG
dict1 = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14}


a = [1 , dict1]


def genA():
    for i in range(5):
        yield i

# print(a[1]['K']+111)
# print(next(genA()))
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'otest.txt')


# testfile = fileinput.FileInput(filename , inplace=True)

# for line in testfile:   
#     if(testfile.filelineno()== 4):
#         print(line.rstrip())
#     else:
#         print(line)
# testfile.close()

# with open(filename, 'a', encoding='utf-8-sig') as testfile:
#     testfile.write('ffff')
#     testfile.write('11111\n')
#     testfile.write('222222')
            