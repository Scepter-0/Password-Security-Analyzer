from menu import display_menu, input_password
from api_checker import times_pwned

def check_password_strength(password):
    count = times_pwned(password)
    if count > 0:
        print(f"\nThis password has appeared in {count} known data breaches.")
    else:
        print("\nThis password has not appeared in any known data breaches.")

def main():
    display_menu()
    password = input_password()
    check_password_strength(password)


if __name__ == "__main__":
    main()
        


