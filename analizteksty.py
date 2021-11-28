import os

filename = "Гаррі Поттер.txt"

def g_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def g_chars(filename):
    with open(filename, encoding="utf8") as file:
        chars = file.read()
    chars = chars.replace("\n", " ")
    chars = chars.lower()
    return chars

def chars_nospace(filename):
    with open(filename, encoding="utf8") as file:
        chars1 = file.read()
    chars1 = chars1.replace("\n", " ")
    chars1 = chars1.lower()
    chars1 = chars1.replace(" ", "")
    return chars1

def g_words_dict(words):
    words_dict = dict()
 
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
 
 
def main(): 
    filename = "Гаррі Поттер.txt"
    words = g_words(filename)
    words_dict = g_words_dict(words)
    characters = g_chars(filename)
    characters1 = chars_nospace(filename) 
    print("Cимволи без пропусків: %d" % len(characters1))
    print("Символи: %d" % len(characters))
    print("Слова: %d" % len(words))
    print("Слова, що не повторюються: %d" % len(words_dict))
    
if __name__ == "__main__":
        main()
        
input()