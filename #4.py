import re
from nltk.stem import PorterStemmer

# Function to normalize and stem text using NLTK
def normalize_and_stem_nltk(text):
    # Remove non-alphabetic characters and convert to lowercase
    normalized_text = re.sub(r'[^a-zA-Z]', ' ', text).lower()

    # Tokenize the text into words
    words = normalized_text.split()

    # Initialize Porter Stemmer
    porter_stemmer = PorterStemmer()

    # Apply stemming to each word
    stemmed_words = [porter_stemmer.stem(word) for word in words]

    # Join the stemmed words to form a paragraph
    processed_paragraph = ' '.join(stemmed_words)

    return processed_paragraph

# Function to normalize and stem text without NLTK
def normalize_and_stem(text):
    # Remove non-alphabetic characters and convert to lowercase
    normalized_text = re.sub(r'[^a-zA-Z]', ' ', text).lower()

    # Tokenize the text into words
    words = normalized_text.split()

    # Apply a simple stemming algorithm (e.g., removing suffix 'ing')
    stemmed_words = [word[:-3] if word.endswith('ing') else word for word in words]

    # Join the stemmed words to form a paragraph
    processed_paragraph = ' '.join(stemmed_words)

    return processed_paragraph

# Read text from a file
file_path = r"C:\Users\Suyash\OneDrive\Documents\NLP Practicals\SamplePara.txt"
with open(file_path, 'r') as file:
    original_text = file.read()

# Display original text
print("Original Text:\n", original_text)

# Task 1: Normalize and stem using NLTK
processed_text_nltk = normalize_and_stem_nltk(original_text)
print("\nProcessed Text with NLTK:\n", processed_text_nltk)

# Task 2: Normalize and stem without NLTK
processed_text_without_nltk = normalize_and_stem(original_text)
print("\nProcessed Text without NLTK:\n", processed_text_without_nltk)

# Save processed data to a file
with open('processed_data_nltk.txt', 'w') as file:
    file.write(processed_text_nltk)

with open('processed_data_without_nltk.txt', 'w') as file:
    file.write(processed_text_without_nltk)

