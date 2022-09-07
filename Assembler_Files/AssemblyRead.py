import os
import re
import Mot_read as mr

registers_name = ['AREG', 'BREG', 'CREG', 'DREG']

def assembler_iter(file_name):
    """
    Iterates through the lines of the assembly file and returns the lines as a list.
    """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '..' , file_name)
    #print(filename)
    with open(filename, 'r') as assembly_file:
        for line in assembly_file:
            #removes empty lines and comments
            if (line.isspace())|(line == '\n')|(line.startswith('#')):
                continue
            line = line.rstrip()
            yield line
            
# label_re = '(?P<label>\w+): )?'
# mnemonics_re = '(?P<Mnemonics>\w+)'
# operand1_re = '( (?P<Operand1>\w+))?'
# operand2_re = '(, (?P<Operand2>\w+))?'




def pattern_match(line):
    pattern2 = '((?P<label>\w+): )?(?P<Mnemonics>\w+)( (?P<Operand1>\w+))?(, (?P<Operand2>\w+))?'
    pattern1 = '(?P<label>\w+) (?P<Mnemonics>D[A-Z]) (?P<Operand1>\w+)'

    pattern_list = [pattern1, pattern2]
    for pattern in pattern_list:
        match = re.match(pattern, line)
        if match:
            return_dict = match.groupdict()
            #for 2nd pattern operand2 is not present so we put none in it
            return_dict['Operand2'] =return_dict.get('Operand2', None)
            return return_dict
    return None



# for a in assembler_iter('sampleAssembly.asm'):
#     print(a)

for a in mr.Mot_dict():
    print(a)
