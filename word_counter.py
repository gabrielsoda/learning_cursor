import re
from collections import Counter


class WordCounter:
    """A class to count words in text files."""
    
    def __init__(self):
        self.text = ""
        self.words = []
        self.word_counts = Counter()
    
    def read_file(self, file_path):
        """
        Read the contents of a text file.
        
        Args:
            file_path (str): Path to the text file to read
            
        Returns:
            bool: True if file was read successfully, False otherwise
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.text = f.read()
            return True
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return False
        except Exception as e:
            print(f"Error reading file: {e}")
            return False
    
    def count_words(self):
        """
        Count words in the loaded text.
        
        Returns:
            int: Total number of words
        """
        if not self.text:
            print("No text loaded. Please read a file first.")
            return 0
        
        # Separate content into words using regex
        self.words = re.findall(r"\w+", self.text.lower())
        
        # Count total number of words
        total_words = len(self.words)
        
        # Create word frequency counter
        self.word_counts = Counter(self.words)
        
        return total_words
    
    def get_most_common_words(self, n=10):
        """
        Get the n most frequent words.
        
        Args:
            n (int): Number of most common words to return
            
        Returns:
            list: List of tuples (word, count) for the most common words
        """
        if not self.word_counts:
            print("No words counted yet. Please call count_words() first.")
            return []
        
        return self.word_counts.most_common(n)
    
    def display_results(self):
        """Display the word count results."""
        if not self.words:
            print("No words to display. Please read a file and count words first.")
            return
        
        total_words = len(self.words)
        print(f"Total words: {total_words}")
        
        most_common_words = self.get_most_common_words(10)
        if most_common_words:
            print("\n10 most frequent words:")
            for word, count in most_common_words:
                print(f"{word}: {count}")


def main():
    """Main function to run the word counter program."""
    # Create WordCounter instance
    word_counter = WordCounter()
    
    # Ask the user for the path to a text file
    file_path = input("Enter the path to the text file: ")
    
    # Read the file
    if word_counter.read_file(file_path):
        # Count words
        total_words = word_counter.count_words()
        
        # Display results
        word_counter.display_results()


if __name__ == "__main__":
    main()



