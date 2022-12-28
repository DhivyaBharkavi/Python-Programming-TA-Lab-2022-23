"""
4.Write a Python program that prompts the user to enter an upper- or lower-case letter and displays the corresponding Unicode encoding.
"""
any_word = str(input("Enter your word "))
print("The current word is ",any_word)
#default unicode encoding
string_uni = any_word.encode()
print("After unicode encoding a word is ",string_uni)
