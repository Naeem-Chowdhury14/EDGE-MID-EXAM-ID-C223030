def generate_anagrams(word):
    # Start with an empty list of anagrams
    anagrams = ['']
    
    # Loop through each character in the word
    for char in word:
        # Create a new list to hold the new anagrams
        new_anagrams = []
        # Create new anagrams by adding the current character to existing anagrams
        for anagram in anagrams:
            for i in range(len(anagram) + 1):
                # Insert the character at each possible position
                new_anagrams.append(anagram[:i] + char + anagram[i:])
        anagrams = new_anagrams  # Update the anagrams list
    
    return anagrams

# Example usage
word = str(input("Enter your string: "))
anagrams = generate_anagrams(word)
print(anagrams)