n = int(input())
str = input()
list_of_words = str.split()
list_of_words_longer_than_n = [word for word in list_of_words if len(word) > n]
print(list_of_words_longer_than_n)
