
#Chase Stratton
#String Assignment : CSCI 111 
#10 points 

#Palindrome Checker Program 
#Palindrome: A word,phrase, or sequence that reads the same forward or backwards.
#This program will check if a given string is a palindrome or not.


# Step 1 : This Will define a function to clean the input and normalize it if needed.
def clean_string(s):
    # Removing the spaces or punctuation, and covert everything to lowercase.
    # This will help focus only on the characters that matter when checking for palindromes.
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    print(f"[DEBUG] Cleaned string: {cleaned}")  # Debugging statement here.
    return cleaned



# Step 2: Defining the main palindrome checking functions.
def is_palindrome(s):
    # Cleaning the input strings by calling the "clean_string" function below
    cleaned = clean_string(s)
    # Check if the cleaned string is equal to its reverse.
    return cleaned == cleaned[::-1]

# Step 3: Adding function to provide creative feedback to the user (UI)
def get_feedback(is_palindrome_result, original_string):
    # If the string is a palindrome, provide positive feedback below.

    if is_palindrome_result:
        return f'"{original_string}" is a palindrome. It reads the same way forwards and back! That\'s cool!'
    else:
        return f'"{original_string}" is not a palindrome. Dont be discouraged—its still a cool phrase. Try again with another one!'


    # Step 4: The main part of the program function where the user interactions occur are is the code below.
def main ():

        # Prompt the user enter a phase or word or numbers that will be checked to see if it is a palindrome or not. While, encouraging the user to to explore different words and phrases to see if they are palindrome or not.
    print("Welcome to the Palindrome checker! Feel free to enter any word or phase or even a sentence into the program ")
while True: 
    user_input = input("Enter a string to check if it's a palindrome (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thanks for using the Palindrome Checker! Goodbye!")
        break 

    # Add a pause for dramatic effect (UI).
    import time 
    print("Checking...")
    time.sleep(1.5)


    # Checking if the input is a palindrome by using the "is_palindrome" function.
    palindrome_result = is_palindrome(user_input)

    # Get creative feedback for the user by calling "get_feedback" function.
    feedback = get_feedback(palindrome_result, user_input)
    print(feedback)


    # tells the user to try again below .
    print("Want to check another one? Just enter it below, or type 'exit' to quit.")



        # Step 5 : This last code is using the typical python idiom to ensure the main function runs when the script is executed thats all. 
if __name__ == "__main__":
    main()


