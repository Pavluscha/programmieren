
def add_tags(tag, word):
    string = "<" + tag + ">" + word + "</" + tag + ">"
    return(string)



print(add_tags('i', 'Python'))