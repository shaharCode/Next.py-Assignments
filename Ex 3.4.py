
import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, character, index):
        self.character = character
        self.index = index

    def __str__(self):
        return f'The username contains an illegal character "{self.character}" at index {self.index}.'


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short."


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long."


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short."


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long."


def check_input(username, password):
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    valid_username_chars = string.ascii_letters + string.digits + '_'
    for index, char in enumerate(username):
        if char not in valid_username_chars:
            raise UsernameContainsIllegalCharacter(char, index)

    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase()
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()

    print("OK")


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
