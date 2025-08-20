import re
from collections import Counter

# Program to count words in a text file

# 1. Ask the user for the path to a text file
# 2. Read the contents of the file
# 3. Separate into words.
# 4. Count total number of words.
# (Optional) Display the 10 most frequent words and their count.

# 1. Ask the user for the path to a text file
file_path = input("Enter the path to the text file: ")

# 2. Read the contents of the file
try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
    exit(1)

# 3. Separate content into words.


words = re.findall(r"\w+", text.lower())

# 4. Count total number of words.
total_words = len(words)



print(f"Total words: {total_words}")


counter = Counter(words)

most_common_words = counter.most_common(10)

print("\n10 most frequent words:")
for word, count in most_common_words:
    print(f"{word}: {count}")



