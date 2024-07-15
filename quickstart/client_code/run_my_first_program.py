from nada_dsl import *
def nada_main():

    party1 = Party(name="Party1")

    # Input a secret integer from Party1
    secret_int = SecretInteger(Input(name="secret_int", party=party1))

    # Convert the secret integer to a string
    secret_str = secret_int.to_string()

    # Reverse the string
    reversed_str = secret_str.reverse()

    # Check if the original string is equal to the reversed string
    is_palindrome = secret_str == reversed_str

    # Output the result as a secret boolean to Party1
    return [Output(is_palindrome, "is_palindrome_output", party1)]
