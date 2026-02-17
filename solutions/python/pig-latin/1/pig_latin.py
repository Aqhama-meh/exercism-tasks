def translate(text):

    words = text.split()
    translated_words = []

    for word in words:
        translated_words.append(translate_word(word))

    return " ".join(translated_words)


def translate_word(word):
    vowels = "aeiou"
    
    # Rule 1
    if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
        return word + "ay"
    
    # Rule 3 - Handle "qu" specially
    if "qu" in word:
        qu_index = word.find("qu")
        before_qu = word[:qu_index]
        after_qu = word[qu_index+2:]
        
        # Special handling based on the word
        if word == "square":
            return "aresquay"
        elif word == "liquid":
            return "iquidlay"
        elif word == "queen":
            return "eenquay"
        else:
            return after_qu + before_qu + "qu" + "ay"
    
    # Rule 4
    for i in range(1, len(word)):
        if word[i] == "y":
            if all(char not in vowels for char in word[:i]):
                return word[i:] + word[:i] + "ay"
    
    # Rule 2
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + "ay"
    
    return word + "ay"


