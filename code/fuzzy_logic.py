# Demonstration file: To show how Fuzzy Library functions works

from thefuzz import fuzz, process

s1="Hello World"
s2="Hello Hello world world world"

print(fuzz.ratio(s1, s2))

print(fuzz.partial_ratio(s1, s2))

print(fuzz.token_sort_ratio(s1,s2))

print(fuzz.token_set_ratio(s1,s2))


things=['Programming language', "Nativ Language", "React Native", "Some Stuff", "Hello world", "Coding stuff"]

print(process.extract("language", things, limit=2))

print(process.extract("stuff some", things, limit=2, scorer=fuzz._token_sort_ratio))