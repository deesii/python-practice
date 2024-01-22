# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

#original submitted 

def is_valid(password):
    special_characters = "!@$%&"
    if len(password) > 7:
        for char in password:
            if char in special_characters:
                return True
        return False
            
    else:
        return False


# print(is_valid("1234567"))

# print(is_valid("12345678"))

# print(is_valid("12345!78"))

#refactored x 1

# def is_valid(password):
#     special_characters = "!@$%&"
#     required_length = 8

#     if len(password) < required_length:
#         return False

#     for char in password:
#         if char in special_characters:
#             return True
    
#     return False


# refactored_code with feedback 
    
def is_valid_refactored(password):
    special_characters = "!@$%&"
    required_length = 8
    return len(password) >= 8 and any(char for char in password if char in special_characters) # boolean output - checks if at least one character in the password is a special character, argument is iterable.

# print(is_valid_refactored("1234567"))

# print(is_valid_refactored("12345678"))

# print(is_valid_refactored("12345!78"))