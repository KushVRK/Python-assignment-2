# Text Analysis Functions
#finding length of the text
def count_words(text):
    words = text.split()
    return len(words)

#finding the number of vowels in the text
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

#finding the number of consonants in the text
def count_consonants(text):
    count = 0
    for ch in text.lower():
        # only count letters that are not vowels
        if ch.isalpha() and ch not in "aeiou":   #it should not include numbers
            count += 1
    return count

#Reversing the text
def reverse_text(text):
    return text[::-1]

#finding text is a palindrome or not
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

#displaying the text without Vowels
def remove_vowels(text):
    result = ""
    for ch in text:
        if ch.lower() not in "aeiou":
            result += ch
    return result

#finding the frequency of each words
def word_frequency(text):
    freq = {}
    words = text.lower().split()
    for word in words:
        # remove punctuation from word
        word = word.strip(".,!?")
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

#finding the longest word in the text
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

#main function includes every text analysis functions
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words        : {count_words(text)}")
    print(f"Vowels       : {count_vowels(text)}")
    print(f"Consonants   : {count_consonants(text)}")
    print(f"Reversed     : {reverse_text(text)}")

    if is_palindrome(text):
        print("Palindrome   : Yes")
    else:
        print("Palindrome   : No")

    print(f"Without vowels: {remove_vowels(text)}")

    lw = longest_word(text)
    print(f"Longest word : {lw} ({len(lw)} letters)")

    # show word frequency as nice string
    
    freq = word_frequency(text)

    freq_list = []

    for key in freq:
        pair = str(key) + ": " + str(freq[key])
        freq_list.append(pair)

    freq_str = ", ".join(freq_list)

    print("Word Frequency:", freq_str)



text = input("Enter text: ")

if text.strip() == "":
    print("Please enter some text!")
else:
    analyze_text(text)