#Program 06 - String Operations

# Accept a string and count vowels and consonants
text = input("Enter a string: ").strip()
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print(f"\nVowels: {vowel_count}, Consonants: {consonant_count}")

# Accept a sentence and find the longest word
sentence = input("\nEnter a sentence: ").strip()
words = sentence.split()
longest = max(words, key=len) if words else "No words found"
print(f"\nLongest word: {longest}")

# Accept a string and print it in reverse
print(f"\nReversed string: {text[::-1]}")

# Convert to title case, uppercase, and lowercase
print(f"\nTitle Case: {text.title()}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
