from itertools import permutations

def isSolvable(words, result):
    max_word_length = max(len(word) for word in words)
    result_length = len(result)
    
    if result_length not in [max_word_length, max_word_length + 1]:
        return False
    
    leading_chars = set()
    for word in words:
        leading_chars.add(word[0])
    leading_chars.add(result[0])
    
    chars = set()
    for word in words:
        chars.update(word)
    chars.update(result)
    chars = list(chars)
    
   