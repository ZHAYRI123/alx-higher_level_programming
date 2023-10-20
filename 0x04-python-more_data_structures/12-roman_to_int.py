#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        romanNum =  {'I': 1, 'V': 5, 'X'; 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rom = roman_string
        i = 0
        result = 0
        for i in range(i, len(rom)):
            if i < len(rom) - 1 and romanNum[rom[i + 1]] > romanNum[rom[i]]:
                result -= romanNum[rom[i]]
            else:
                result += romanNum[rom[i]]
        return result
    else:
        return 0
