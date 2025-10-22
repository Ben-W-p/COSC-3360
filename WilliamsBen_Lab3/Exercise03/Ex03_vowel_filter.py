def only_vowels(s: str):
    return list(filter(lambda ch: ch in 'aeiouAEIOU', s))

str1 = 'Computer Science'
vowels = only_vowels(str1)
print("Source:", str1)
print("Vowels (as list):", vowels)
print("Vowels (joined):", ''.join(vowels))
