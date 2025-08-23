import re
from collections import Counter


class WordCounter:
    """A class to count words in text files."""
    
    def __init__(self):
        self.text = ""
        self.words = []
        self.word_counts = Counter()
        # Spanish connector words (stop words) to exclude from counting
        self.stop_words = {
            'de', 'la', 'y', 'el', 'en', 'que', 'qué', 'a', 'del', 'un', 'por',
            'con', 'se', 'no', 'te', 'lo', 'le', 'da', 'su', 'me', 'mi',
            'es', 'son', 'las', 'los', 'una', 'como', 'pero', 'sus', 'has',
            'han', 'hay', 'está', 'están', 'fue', 'fueron', 'ser', 'era',
            'eran', 'tiene', 'sin', 'hace', 'dice', 'dicen', 'para', 'entre', 'al'
        }
    
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
        Count words in the loaded text, excluding connector words.
        
        Returns:
            int: Total number of meaningful words (excluding connectors)
        """
        if not self.text:
            print("No text loaded. Please read a file first.")
            return 0
        
        # Separate content into words using regex
        all_words = re.findall(r"\w+", self.text.lower())
        
        # Filter out stop words and store meaningful words
        self.words = [word for word in all_words if word not in self.stop_words]
        
        # Count total number of meaningful words
        total_words = len(self.words)
        
        # Create word frequency counter for meaningful words only
        self.word_counts = Counter(self.words)
        
        return total_words
    
    def get_most_common_words(self, n=20):
        """
        Get the n most frequent meaningful words.
        
        Args:
            n (int): Number of most common words to return
            
        Returns:
            list: List of tuples (word, count) for the most common meaningful words
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
        print(f"Total meaningful words (excluding connectors): {total_words}")
        
        most_common_words = self.get_most_common_words(20)
        if most_common_words:
            print("\n10 most frequent meaningful words:")
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
        word_counter.count_words()
        
        # Display results
        word_counter.display_results()


if __name__ == "__main__":
    main()



