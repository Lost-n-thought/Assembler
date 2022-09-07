Tables - CSV

### ASM file

#### line splitting

```
START 200
NEXT: ADD AREG, BREG
SUB AREG, NUMBER
ADD BREG , 5

JUMP NEXT
NUMBER DC 5
CONS1 DC 1
ARRAY DS 10
END
```

line format

| Label                                      | Mnemonics   | operand1                                                         | operand2                                   |
| ------------------------------------------ | ----------- | ---------------------------------------------------------------- | ------------------------------------------ |
| [Label[:] ]                                | Mnemonics   | [operand1]                                                       | [, operand2]                               |
| Anylength                                  | max4letters | Anylength                                                        | Anylength                                  |
| Alphanumeric(must start with letter or __) | Aplhabets   | Alphanumeric(must start with letter or __) or number or [symbol] | Alphanumeric(must start with letter or __) |
|                                            |             |                                                                  |                                            |

#### Python regex

Label               - '([A-Z0-9]+: )?'

Mnemonics           - '[A-Z]{,4}'

operand1            - '( [A-Z0-9].)?'

operand2            - '(, [A-Z0-9].)?'

operand combined    - '(([A-Z0-9].)(, [A-Z0-9].)?)?'

re.findall(r'([A-Z0-9]+: )?[A-Z]{,4}( [A-Z0-9].)?(, [A-Z0-9].)?', line)



LC processing

 Symbol Table


