from stats import get_word_count, get_character_count, get_sorted_dict

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  book = 'books/frankenstein.txt'
  book_text = get_book_text(book)
  word_count = get_word_count(book_text)
  char_counts = get_character_count(book_text)
  sorted_alpha_counts = get_sorted_dict(char_counts)

  # Create report
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for item in sorted_alpha_counts:
    char = item["char"]
    num = item["num"]
    print(f"{char}: {num}")
  print("============= END ===============")

main()