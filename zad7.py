words_list = ["hello", "world", "kittyy", "hi", "elo"]

long_world = list(filter(lambda x: len(x) > 5, words_list))


print(long_world)