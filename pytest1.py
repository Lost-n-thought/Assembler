import Assembler_Files.Mot_read as AF
import re

#print(dir(AF))
mot_file = list(AF.return_Mot())
#print(mot_file)



pattern2 = '((?P<label>\w+): )?(?P<Mnemonics>\w+)( (?P<Operand1>\w+))?(, (?P<Operand2>\w+))?'
pattern1 = '(?P<label>\w+) (?P<Mnemonics>D[A-Z]) (?P<Operand1>\w+)'

pattern_list = [pattern1, pattern2]

def pattern_match(line , pattern_list = pattern_list):
    for pattern in pattern_list:
        match = re.match(pattern, line)
        if match:
            return match
    return None

line1 = 'NEXT: ADD AREG, BREG'

#print(pattern_match(line1).groupdict())

with open('sampleAssembly.asm') as asm:
    for line in asm:
        if(line == "\n"):
            continue
        print(pattern_match(line).groupdict())