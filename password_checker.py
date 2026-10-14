from menu import display_menu, input_password
from api_checker import times_pwned

def check_password_databreach(password):
    count = times_pwned(password)
    if count > 0:
        print(f"\nThis password has appeared in {count} known data breaches.\n")
    else:
        print("\nThis password has not appeared in any known data breaches.\n")

def check_password_strength(password):
    score = 10
    length = len(password)
    #checks whether the password has uppercase, lowercase, special characters, and numbers and gives a boolean value for each.
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special_char = any(char in "!@#$%^&*()-+" for char in password)
    has_number = any(char.isdigit() for char in password)

    if length < 8:
        score -=2
        length_score = "Weak"
    if has_upper == False:
        score -= 2
        upper_score = "Weak"
    if has_lower == False:
        score -= 2
        lower_score = "Weak"
    if has_special_char == False:
        score -= 2
        special_score = "Weak"
    if has_number == False:
        score -= 2
        number_score = "Weak"

    print(f"\nPassword Strength Score: {score}/10")

    if score >= 8:
        print("Password Strength: Strong")
    elif score >= 5:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Weak")

    info = input("\nWould you like to see suggestions for improving your password? (y/n): ")

    if info.lower() == "y":
        print("\nSuggestions for improving your password:")
        if length < 8:
            print("- Increase the length of your password to at least 8 characters.")
        if not has_upper:
            print("- Include at least one uppercase letter.")
        if not has_lower:
            print("- Include at least one lowercase letter.")
        if not has_special_char:
            print("- Include at least one special character (e.g., !@#$%^&*()-+).")
        if not has_number:
            print("- Include at least one number.")
    else:
        print("\nNo suggestions will be provided. Thank you for using the Password Strength Checker!")
    

def main():
    display_menu()
    password = input_password()
    check_password_databreach(password)
    check_password_strength(password)

if __name__ == "__main__":
    main()