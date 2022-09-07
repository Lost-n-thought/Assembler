



### Assembly file Reader

##### Features

1. Supports Comment line
   1. Comment line start with "#" .
   2. thery can be white space before "#"
2. Supports Empty file

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

#### line format

| Label                                      | Mnemonics   | operand1                                                         | operand2                                   |
| ------------------------------------------ | ----------- | ---------------------------------------------------------------- | ------------------------------------------ |
| [Label[:] ]                                | Mnemonics   | [operand1]                                                       | [, operand2]                               |
| Anylength                                  | max4letters | Anylength                                                        | Anylength                                  |
| Alphanumeric(must start with letter or __) | Aplhabets   | Alphanumeric(must start with letter or __) or number or [symbol] | Alphanumeric(must start with letter or __) |
|                                            |             |                                                                  |                                            |





LC processing

 Symbol Table

