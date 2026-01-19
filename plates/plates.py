#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
punctuation = "!@#$%^&*()-=_+[]|:';?/<>., "

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = s.lower()
    if length_check(s):
        if char_start_check(s):
            if punctuation_check(s):
                if num_mid_check(s):
                    return True

def char_start_check(s):
    if s[0] in alphabet:
        if s[1] in alphabet:
            return True
        
def length_check(s):
    length = len(s)
    if 2 <= length <= 6:
        return True

def punctuation_check(s):
    for char in s:
        if char in punctuation:
            return False
    return True

def num_mid_check(s):
    char_position = 0
    for char in s:
        if char in numbers:
            char_position = char.find(numbers)
            if s[char_position] == s[-1]:
                return True
            next_char = char_position + 1
            break

    if next_char in alphabet:
        return False

#    if s[index] == s[-1]:
#        return True
#    if s[index] in alphabet:
#        return False
#    else:
#        return True

main()