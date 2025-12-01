def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(filepath):
    book = get_book_text(filepath)
    word_count = len(book.split())
    return (f"Found {word_count} total words")
    
def get_char_count(filepath):
    file_str = get_book_text(filepath).lower()
    count_dict = {}
    counter = 0
    for char in file_str:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def get_sort_dict(char_dict):
    char_list = [{'char': key, 'num': value} for key, value in char_dict.items()]
    
    def get_count(item):
        return item['num']
    
    char_list.sort(key=get_count, reverse=True)
    
    return char_list