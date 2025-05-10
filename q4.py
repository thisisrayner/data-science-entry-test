# q4.py
# Problem: Dictionaries - Word Frequency Counter
# Write a Python script that takes a sentence (string) as input and
# counts the frequency of each word in the sentence.
# The output should be a dictionary where keys are words and values are their frequencies.
# Ignore case (e.g., "The" and "the" should be counted as the same word).
# Punctuation should be removed or handled simply.

import string # To help with punctuation removal

def count_word_frequency(sentence):
    """
    Counts the frequency of each word in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    if not isinstance(sentence, str) or not sentence.strip():
        print("Input must be a non-empty string.")
        return {}

    print(f"Original sentence: \"{sentence}\"")

    # 1. Convert to lowercase
    processed_sentence = sentence.lower()

    # 2. Remove punctuation
    # A simple way is to replace common punctuation marks with a space or nothing
    # For a more robust solution, one might use regular expressions
    translator = str.maketrans('', '', string.punctuation)
    processed_sentence = processed_sentence.translate(translator)
    # print(f"After lowercase and punctuation removal: \"{processed_sentence}\"")

    # 3. Split the sentence into words
    words = processed_sentence.split() # Splits by whitespace
    # print(f"Words list: {words}")

    # 4. Count word frequencies
    word_counts = {}
    for word in words:
        if word: # Ensure word is not empty (can happen with multiple spaces)
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

if __name__ == "__main__":
    print("--- Word Frequency Counter ---")

    sentence1 = "This is a test sentence. This test is simple."
    frequencies1 = count_word_frequency(sentence1)
    print(f"Word frequencies: {frequencies1}\n")
    # Expected: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'sentence': 1, 'simple': 1}

    sentence2 = "The quick brown fox jumps over the lazy dog. The dog barks."
    frequencies2 = count_word_frequency(sentence2)
    print(f"Word frequencies: {frequencies2}\n")
    # Expected: {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'barks': 1}

    sentence3 = "  Spaces   and   more spaces  "
    frequencies3 = count_word_frequency(sentence3)
    print(f"Word frequencies: {frequencies3}\n")
    # Expected: {'spaces': 2, 'and': 1, 'more': 1}

    sentence4 = "" # Empty sentence
    frequencies4 = count_word_frequency(sentence4)
    print(f"Word frequencies for empty sentence: {frequencies4}\n")
    # Expected: {} (with "Input must be a non-empty string." message)

    sentence5 = "Hello!"
    frequencies5 = count_word_frequency(sentence5)
    print(f"Word frequencies: {frequencies5}\n")
    # Expected: {'hello': 1}

# Test Cases:
# 1. "Hello world Hello" -> {'hello': 2, 'world': 1}
# 2. "Go Catz Go!" -> {'go': 2, 'catz': 1}
# 3. "" -> {}
