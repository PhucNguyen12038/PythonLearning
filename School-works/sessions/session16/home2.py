import re

def is_strong(password):
    
    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error )

    if password_ok:
        return True
    else:
        return False

#print(is_strong("k4A8cd82B"))
#print(is_strong("Bdy5Cez"))
#print(is_strong("password"))