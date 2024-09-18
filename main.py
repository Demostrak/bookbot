# Description: This is a bookbot program for Boot.dev

def main():
    with open("./books/frankenstein.txt", 'r') as f:
        file_contents = f.read()
        # print(file_contents)

        # Count the number of words in the file
        def count_words(file_contents):
            return len(file_contents.split())   

        # Count the number of characters in the file
        def count_characters(file_contents):
            return len(file_contents)   
        
        # Print the numbers of each letter in the file
        def count_letters(file_contents):
            lower_contents = file_contents.lower()
            letters = {}
            for letter in lower_contents:
                if letter.isalpha():
                    if letter in letters:
                        letters[letter] += 1
                    else:
                        letters[letter] = 1
            return letters

        # Sort the letters in the file
        def sort_letters(file_contents):
            letters = count_letters(file_contents)
            sorted_letters = dict(sorted(letters.items()))
            return sorted_letters
    

        print("--- Begin report of books/frankenstein.txt ---/n/n")
        print("The number of words in the file is: ", count_words(file_contents))
        print(f"The number of characters in the file is: {count_characters(file_contents)} \n\n")
        #print("The number of each letter in the file is: ", count_letters(file_contents))
        #print("The sorted letters in the file are: ", sort_letters(file_contents))

        for letter, count in sort_letters(file_contents).items():
            print(f"The letter '{letter}' was found {count} times in the file.")

        print("\n--- End report of books/frankenstein.txt ---")
if __name__ == "__main__":
    main()
