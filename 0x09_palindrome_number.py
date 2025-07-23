"""
Palindrome Number Solution
Words from Pungent - "I'd rather just convert x to a string, but it's more leet with math."
"""
def main() -> None:
    print(isPalindrome(77171777))

def isPalindrome(x: int) -> bool:
    reversed = 0
    origin = x 

    while x > 0: # Stop loop when x is fully reversed
        digit = x % 10 # Get last digit of x
        reversed = reversed * 10 + digit # Shift left and add digit
        x //= 10 # Moving to the next decimal place (121 -> 12)

    return reversed == origin

main()
