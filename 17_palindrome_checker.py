# Palindrome Checker

word = input("Enter word/number: ")

# converting the word to lowercase to ignore case
cleaned = word.lower()

# reverse it to check palindrome
reversed_word = cleaned[::-1]

print(f"\nOriginal : {word}")
print(f"Reversed : {word[::-1]}")

# Displaying step by step verification
print("\nStep by step verification:")
print(f"Lower cased original word/number: {cleaned}")
print(f"Lower cased reversed word/number: {reversed_word}")

if cleaned == reversed_word:
    print(f"\nResult: PALINDROME")
else:
    print(f"\nResult: NOT a palindrome")