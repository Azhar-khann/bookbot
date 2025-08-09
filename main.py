from stats import count_words 
from stats import count_char
from stats import sort_count_char
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_name):
    with open(file_name, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
    return get_book_text(sys.argv[1])  


print('============ BOOKBOT ============')
print('Analyzing book found at ' + sys.argv[1])
print('----------- Word Count ----------')
print('Found ' + str(count_words(main())) + ' total words')
print('----------- Character Count ----------')
sorted_char_count = sort_count_char(count_char(main()))
for char_dict in sorted_char_count:
    for char in char_dict:
        print(char + ': ' + str(char_dict[char]))

print('==================================')
