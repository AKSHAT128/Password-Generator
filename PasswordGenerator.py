import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_from_words(words):
    substitutions = {'S': ['5', '$'], 'I': ['1', 'i'], 'A': '@', 'E': '3', 'G': '6', 'B': '8', 'H': '#', 'R': '&', 'U': '(', 'V': ')'}
    password = ''

    first_letter = words[0][0].lower() if words[0][0].isalpha() else random.choice(['$', '#', '@', '(', ')'])
    password += first_letter

    for word in words:
        for letter in word:
            if letter.upper() in substitutions.keys():
                letter = random.choice(substitutions[letter.upper()])
            password += letter
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    return password

def get_user_choice():
    print("Choose an option:")
    print("1. Generate a random password of specified length")
    print("2. Generate a password based on provided words")
    choice = input("Enter option (1 or 2): ")
    return choice

def get_user_words():
    user_input = input("Enter words to generate password (separate with space): ")
    words = user_input.split()
    return words

while True:
    choice = get_user_choice()

    if choice == '1':
        length = int(input("Enter the length of the password (minimum 8 characters recommended): "))
        if length < 8:
            print("Minimum length should be 8 characters. Please try again.")
            continue
        password = generate_random_password(length)
    elif choice == '2':
        user_words = get_user_words()
        password = generate_password_from_words(user_words)
    else:
        print("Invalid choice. Please try again.")
        continue

    print("Generated Password:", password)
    
    restart = input("Do you want to generate another password? (yes/no): ")
    if restart.lower() != 'yes':
        break
