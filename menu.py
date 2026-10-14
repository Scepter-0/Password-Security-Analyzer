def display_menu():
    print(f"\nWelcome to the Password Strength Checker!\n\nCreated By:\n")

    print("""
    ███████╗ ██████╗███████╗██████╗ ████████╗███████╗██████╗ 
    ██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
    ███████╗██║     █████╗  ██████╔╝   ██║   █████╗  ██████╔╝
    ╚════██║██║     ██╔══╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██╗
    ███████║╚██████╗███████╗██║        ██║   ███████╗██║  ██║
    ╚══════╝ ╚═════╝╚══════╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝
    """)

    print("\n-This tool checks if a password has been compromised in known data breaches using the 'Have I Been Pwned' API. It also will rate your password strength and provide suggestions for improvement.\n-Please note that this tool does not store or log any passwords entered. Your privacy and security are my top priorities.\n-Let's get started! Please enter a password to check its strength and see its compromise status, strength and if there are any improvements needed.\n")

def input_password():
    password = input("Enter a password to check: ")
    return password

