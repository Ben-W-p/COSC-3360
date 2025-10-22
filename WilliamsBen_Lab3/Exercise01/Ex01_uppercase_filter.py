def only_upper(s: str):
    return list(filter(lambda ch: 'A' <= ch <= 'Z', s))

str1 = 'Computer Science'
uppers = only_upper(str1)
print("String:", str1)
print("Uppercase characters:", uppers)