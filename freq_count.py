input_line=input("enter a string:")
words_dict={}
for word in input_line.split():
    words_dict[word]=words_dict.get(word,0)+1
for key in sorted(words_dict):
    print("{}:{}".format(key,words_dict[key]))

