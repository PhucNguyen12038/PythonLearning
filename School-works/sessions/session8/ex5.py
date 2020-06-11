from urllib.request import urlopen

def find_longest_word(word_list):  
    longest_word = ''
    length = 0
    max_length = 0
    for word in word_list:    
          length = len(word)
          if length > max_length:
              longest_word = word
              max_length = length
    print("The longest word is {}".format(longest_word))
name = input("Enter URL: ")
urlfile = urlopen(name)
urlbytes = urlfile.read()
text = urlbytes.decode()
count_line = 0

print("The file contains {} lines".format(text.count("\n")))
print("The word 'war' occurs {} times.".format(text.count("war")))
print("The word 'peace' occurs {} times.".format(text.count("peace")))
word_list = text.split()  
find_longest_word(word_list)  


urlfile.close()