def get_num_words(): 
    filepath = 'books/frankenstein.txt'
    word_count = 0
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)
        for words in file_contents.split():
            word_count += 1
        return (f"{word_count} words found in the document")