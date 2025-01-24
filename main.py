# Function to read the contents of the file and return the text
def main():
    # Open the specified text file and read its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # Print the file contents for reference
        print(file_contents)
        # Return the file contents as a string
        return file_contents

# Function to count the number of words in the given text
def num_words(file_contents):
    # Split the text into words and count them
    words = len(file_contents.split())
    # Print the total number of words
    print("Number of words:", words)

# Function to count the frequency of each alphabetic character in the text
def count_characters(file_contents):
    # Convert the text to lowercase for case-insensitive counting
    file_contents = file_contents.lower()
    # Initialize an empty dictionary to store character counts
    char_counts = {}
    # Iterate through each character in the text
    for char in file_contents:
        # Check if the character is alphabetic
        if char.isalpha():  
            # Increment the count if the character already exists in the dictionary
            if char in char_counts:
                char_counts[char] += 1
            # Otherwise, add the character to the dictionary with an initial count of 1
            else:
                char_counts[char] = 1
    # Return the dictionary containing character counts
    return char_counts

# Function to convert the character counts dictionary into a list of dictionaries
def convert_to_list(char_counts):
    # Use a list comprehension to transform the dictionary into a list of dictionaries
    char_list = [{"character": char, "count": count} for char, count in char_counts.items()]
    # Return the list of dictionaries
    return char_list

# Function to sort the list of dictionaries by a specified key
def sort_characters(char_list, sort_by="count", reverse=True):
    # Sort the list based on the specified key (default is 'count') in descending order
    return sorted(char_list, key=lambda x: x[sort_by], reverse=reverse)

# Main script execution starts here
# Read the file contents into the 'text' variable
text = main()

# Calculate and print the number of words in the text
num_words(text)

# Count the frequency of each alphabetic character in the text
char_counts = count_characters(text)

# Print the character counts stored in the dictionary
print("\nCharacter Counts (Dictionary):")
for char, count in char_counts.items():
    print(f"'{char}': {count}")

# Convert the character counts dictionary into a list of dictionaries
char_list = convert_to_list(char_counts)

# Sort the list of dictionaries by character count in descending order
sorted_char_list = sort_characters(char_list)

# Print the sorted list of character counts
print("\nCharacter Counts (Sorted List):")
for entry in sorted_char_list:
    print(f"Character: '{entry['character']}', Count: {entry['count']}")





'''
Solution files code from Boot.dev

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
'''