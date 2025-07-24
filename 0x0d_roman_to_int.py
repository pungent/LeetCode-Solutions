"""
XIII. Roman to Integer - Given a roman numeral, convert it to an integer.
Words from Pungent: "I spent far more time on this than I should have."
"""
def main() -> None:
    print(romanToInt("I"))

def romanToInt(roman_string) -> int:
    conversion = 0 
    roman_numerals = {
        "I" : 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i in range(len(roman_string)):
        current_char = roman_string[i]
        if i + 1 < len(roman_string): # Prevent index from going out of range
            next_char = roman_string[i + 1]
            if roman_numerals[current_char] < roman_numerals[next_char]: # When a number is smaller than the next, subtract from total. This lets IX equal 9 and not 11
                    conversion -= roman_numerals[current_char]
            else: # If our number were X then this would be '0 + 10'
                conversion += roman_numerals[current_char]
        else: # Exception for a 1 character long roman numeral
             conversion += roman_numerals[current_char]
    return conversion

main()
