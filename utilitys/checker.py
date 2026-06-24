import re

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
password_pattern = pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@&])[A-Za-z\d@&]{6,}$"

def check(password,email):
    check_email = re.fullmatch(email_pattern,email)
    check_password = re.fullmatch(password_pattern,password)

    if check_email and check_password:
        return True
    else:
        return False














