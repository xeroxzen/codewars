def duplicate_encoder(word):
    result = ""
    for each in word:
        if word.count(each.lower()) > 1 or word.count(each.upper()) > 1:
            result += ")"
        else:
            result += "("
        return result
