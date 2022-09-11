import AssemblyRead as AR
import SymbolTableGenration as SG

SG.create_symbol_table()
for line11 in AR.final_asm_line_dict_list('sampleAssembly.asm'):
    print(line11)
