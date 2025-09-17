def get_word_count(text: str):
  words = text.split()
  return len(words)

def get_character_count(text: str):
  character_count = {}
  for character in text:
    current_char = character.lower()
    if(current_char in character_count):
      character_count[current_char] += 1
    else:
      character_count[current_char] = 1
  return character_count

def sort_on(items):
  return items["num"]

def get_sorted_dict(unsorted_dict: dict):
  sorted_dicts = []
  for (char, count) in unsorted_dict.items():
    if(char.isalpha()):
      sorted_dicts.append({"char": char, "num": count})
  sorted_dicts.sort(reverse=True, key=sort_on)
  return sorted_dicts