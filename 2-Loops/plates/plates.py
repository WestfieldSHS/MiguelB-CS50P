#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
punctuation = "!@#$%^&*()-=_+[]|:';?/<>., "

# use of arguments to make it look cleaner.
def main():
    plate = input("Plate: ")
    if is_valid(plate): # automatically assumes it means == True
        print("Valid")
    else:
        print("Invalid")

# s is the placeholder name for plate
# makes the plate lowercase so that checks are easier
# before calling the functions necessary for the checks
def is_valid(s):
    s = s.lower()
    if length_check(s):
        if char_start_check(s):
            if punctuation_check(s):
                if num_mid_check(s):
                    return True

# gets length of plate and makes sure its between 2 n 6 inclusive
def length_check(s):
    length = len(s)
    if 2 <= length <= 6:
        return True

# checks to see if the first two chars of plate are letters
def char_start_check(s):
    if s[0] in alphabet:
        if s[1] in alphabet:
            return True

# cycles thru every char in plate to make sure its not a punctuation mark
def punctuation_check(s):
    for char in s:
        if char in punctuation:
            return False
    return True

def num_mid_check(s): # this was the most complicated one i struggled
    char_position = 0
    for char in s:
        if char in numbers:
            # checks to see if the number is the last char in the plate which is auto valid
            if s[char_position] == s[-1]:
                return True
            # gets the char position of the character after it
            next_char = char_position + 1
            # terminates the loop, telling the programme to go to the if statement
            # essentially the loop only wants the FIRST instance of a number that isnt the last char
            break
        else:
            # if its a letter, it carries on
            char_position = char_position + 1
    # sees if the char after the number is a letter, which is not allowed.
    if s[next_char] in alphabet:
        return False

# AB1CD2 is invalid however AB1CD1 would not be because s[2] = s[-1] since 1=1 uh oh
main()