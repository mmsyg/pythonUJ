def roman2int(roman):
    previous_value = 0
    result = 0
    roman_number = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for char in roman[::-1]:
        if roman_number[char] >= previous_value:
            result += roman_number[char]
        else:
            result -= roman_number[char]
        previous_value = roman_number[char]

    return result


print(roman2int('XCIV'))
